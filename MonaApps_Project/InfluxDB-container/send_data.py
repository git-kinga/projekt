import requests
import json
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import time

class Sender():
    def __init__(self, url) -> None:
        self.influx_token = '6WMK_s0YqTbbaGR5OQ2rStrdG45nusGsTXoLHkLVp0danin8Idq4DGRhLn3_Y37b9jpZAQ9dcezBVvWPkWCCcg=='
        self.server_token = 'C1HkSXTO8AiWVjD2axX0fTLz29KrbICOEWYtvwUEQw2ejhfZit73igjEz7iwMyhO'
        self.url = url
        self.client = InfluxDBClient(url='localhost:8086', token=self.influx_token, org='my-org')
        self.bucket = 'users_tokens'
        
    def get_user_tokens(self, token: str):
        try:
            response = requests.post(self.url, headers={'Authorization' : token})
        except:
            response = '{}'
            
        return json.loads(response.text)
    
    def format_dict(self, data: dict) -> str:
        return '\n'.join([f'user_tokens user="{user}",token="{token}" {time.time_ns()+ind}' 
                          for ind, (user, token) in enumerate(data.items())])
    
    def send_tokens(self, line_protocol):
        # write_api = self.client.write_api(write_options=SYNCHRONOUS)
        # write_api.write(bucket=self.bucket, org='my-org', record=line_protocol)
        # print("send_tokens")
        with InfluxDBClient('http://localhost:8086/', self.influx_token) as client:
            # use the client to access the necessary APIs
            # for example, write data using the write_api
            with client.write_api() as writer:
                writer.write(bucket=self.bucket, org='my-org', record=line_protocol)
            
    def run(self):
        data = self.get_user_tokens(self.server_token)
        line_protocol = self.format_dict(data)
        print(line_protocol)
        self.send_tokens(line_protocol)
              
        
def main():
    obj = Sender('http://localhost:8000/influx/get_tokens/')
    obj.run()

if __name__ == '__main__':
    main()


'''
from(bucket: "users_tokens")
  |> range(start: -1d)
  |> filter(fn: (r) => r._measurement == "user_tokens")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> keep(columns: ["user", "token"])'''