import requests
import time
import json
import os
import sys

class Agent:
    def __init__(self):
        self.urls = []
        self.agent_token = os.getenv('UNIQUE_TOKEN')
        self.agent_name = os.getenv('USERNAME')
        self.config_pull_url = f"http://host.docker.internal:8000/api/config/{self.agent_name}"
        self.message = "Error while collecting data"

    def get_config(self):
        try:
            response = requests.post(self.config_pull_url, headers={'Authorization' : self.agent_token})
        except Exception as error:
            pass

        if response.status_code == 200:
            self.urls=json.loads(response.text)
            return json.loads(response.text)
        else:
            return None

    def format_string(self, string, *args, **kwargs):
        print(string, type(string))
        if type(string) == str:
            print(string.replace(' ', '\\ ').replace(',', '\\,').replace('"', '\\"').replace('=','\\='))
            return string.replace(' ', '\\ ').replace(',', '\\,').replace('"', '\\"').replace('=','\\=')
        return string
        
    def save(self, data):
        measures = []
        if data:
            for ind, (id, values) in enumerate(data.items()):
                user, url, status = tuple(map(self.format_string, values))

                measures.append(f'site_status,agent_tok="tag-to-replace",user_name="{user}",url="{url}" status="{status}" {time.time_ns()+ind}')

                print(measures)
                
            line_protocol = '\n'.join(measures) + '\n'
            
            with open('/app/output.txt', "w") as file:
                try:
                    file.write(line_protocol)
                    self.message = "No error"
                except:
                    self.message = "Error while saving data to save"
                    
        
    def run(self):
        self.urls = self.get_config()
        data={}
        if self.urls is None:
            return
        
        for id, (user, url) in self.urls.items():
            data[id]=[user, url]
            url = url if url.startswith('http') else 'https://' + url
            try:
                response = requests.get(url)
                status_code = response.status_code
            except:
                status_code = 404
            data[id].append(status_code)
            
        self.save(data)
    
        return self.message

def main():
    agent = Agent()
    return agent.run()


if __name__ == "__main__":
    sys.exit(main())