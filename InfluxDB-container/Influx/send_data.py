import requests
import json
from influxdb_client import InfluxDBClient
import time

def read_keys(file_path):
    with open(file_path, 'r') as file:
        api_key, server_key = file.readlines()
    return api_key[api_key.index(':')+1:].strip().strip('"'), server_key[api_key.index(':')+1:].strip().strip('"')

class Sender():
    def __init__(self, url, path_file=r'/app/api_keys') -> None:
        self.influx_token, self.server_token = read_keys(path_file)
        self.url = url
        self.bucket = 'users_tokens'
        
    def get_user_tokens(self, token: str):
        try:
            response = requests.post(self.url, headers={'Authorization' : token})
        except Exception as e:
            print(e)
            print('Getting users token')
            response = {}
            
        return json.loads(response.text)
    
    def format_dict(self, data: dict) -> str:
        timestamp = time.time_ns()
        return '\n'.join([f'agent_tokens,agent_name="{user}" agent_tok="{token}" {timestamp+ind}' 
                          for ind, (user, token) in enumerate(data.items())])
    
    def send_tokens(self, line_protocol):
        if line_protocol:
            print("Trying to send tokens")
            with InfluxDBClient('http://host.docker.internal:8086/', self.influx_token) as client:
                with client.write_api() as writer:
                    writer.write(bucket=self.bucket, org='my-org', record=line_protocol)
                    print("DATA_SENT")

        else: print("There is no new data to send")
        
    def get_existing_data(self):
      with InfluxDBClient('http://host.docker.internal:8086/', self.influx_token) as client:
        query_api = client.query_api()
        query = '''
            from(bucket: "users_tokens")
                |> range(start: 0)
                |> filter(fn: (r) => r._measurement == "agent_tokens")
                |> last()
        '''
        
        tables = query_api.query(org='my-org',query=query)
        existing_data = {}

        for table in tables:
            for record in table.records:
                user = record.values['agent_name'].strip('"')
                token = record.values['_value'].strip('"')
                if user not in existing_data:
                    existing_data[user] = token

        return existing_data
    
    def compare_data(self, existing_data, incoming_data):
        updated_users = {}
        
        for user, token in incoming_data.items():
            if user in tuple(existing_data.keys()):
                if token != existing_data[user]:
                    print("NEW TOKEN")
                    updated_users[user] = token
            else: 
                print("NEW USER")
                updated_users[user] = token
                
        return updated_users
    
            
    def run(self):
        incoming_data = self.get_user_tokens(self.server_token)
        existing_data = self.get_existing_data()
        updated_users = self.compare_data(existing_data, incoming_data)
        line_protocol = self.format_dict(updated_users)
        self.send_tokens(line_protocol)
              
        
def main():
    obj = Sender('http://host.docker.internal:8000/influx/get_tokens/')
    obj.run()

if __name__ == '__main__':
    main()


