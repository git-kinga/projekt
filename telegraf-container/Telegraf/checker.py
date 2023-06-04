import requests
import time
import json
import os

class Agent:
    def __init__(self):
        self.urls = []
        self.agent_token = os.getenv('UNIQUE_TOKEN')
        self.agent_name = os.getenv('USERNAME')
        self.config_pull_url = f"http://host.docker.internal:8000/api/config/{self.agent_name}"

    def get_config(self):
        try:
            response = requests.post(self.config_pull_url, headers={'Authorization' : self.agent_token})
        except Exception as error:
            print(error)
        
        if response.status_code == 200:
            self.urls=json.loads(response.text)
            return json.loads(response.text)
        else:
            return None

    def save(self, data):
        if data:
            line_protocol = '\n'.join([f'site_status,users_tag="tag-to-replace" url="{url}",status="{status}" {time.time_ns()+ind}' 
                                    for ind, (url, status) in enumerate(data.items())]) + '\n'
            
            with open('/app/output.txt', "w") as file:
                file.write(line_protocol)
        
    def run(self):
        self.urls = self.get_config()
        data={}
        
        if self.urls is None:
            print("Error: Could not retrieve config")
            return
        
        for url in self.urls.values():
            url = url if url.startswith('http') else 'https://' + url
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data[url]=response.status_code
                else:
                    data[url]=response.status_code
            except:
                print(f"{url} Failed to establish a new connection")
                data[url]='error'
        
        json_data=json.dumps(data)
        self.save(data)
        
        return json_data

def main():
    agent = Agent()
    json_data=agent.run()
    print(json_data)

if __name__ == "__main__":
    main()
    