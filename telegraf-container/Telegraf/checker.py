import requests
import time
import json
import os
import sys

class Agent:
    def __init__(self):
        self.urls = []
        self.agent_token = "wGWAGew4DUGaxPQGt5x5bBhfKRjFbsaM"
        self.agent_name = "user01"
        self.config_pull_url = f"http://localhost:8000/api/config/{self.agent_name}"
        self.message = "Error while collecting data"

    def get_config(self):
        """Function that connects with api_endpoint to get sites to monitor

        Returns:
            dictionary: key-value pairs of task id and list of parameters that telegraf need
        """
        
        try:
            response = requests.post(self.config_pull_url, headers={'Authorization' : self.agent_token})
        except Exception as error:
            return None

        if response.status_code == 200:
            self.urls=json.loads(response.text)
            return json.loads(response.text)
        else:
            return None

    def format_string(self, string, *args, **kwargs):
        """function to format sting that line protocol can read

        Args:
            string (string): string to format

        Returns:
            string: formatted string
        """
        print(string, type(string))
        if type(string) == str:
            print(string.replace(' ', '\\ ').replace(',', '\\,').replace('"', '\\"').replace('=','\\='))
            return string.replace(' ', '\\ ').replace(',', '\\,').replace('"', '\\"').replace('=','\\=')
        return string
        
    def save(self, data):
        """Function that saves data to file, that telegraf read

        Args:
            data (dictionary): key-value pairs of task and list of parameters and results
        """
        measures = []
        if data:
            for ind, (id, values) in enumerate(data.items()):
                user, url, status = tuple(map(self.format_string, values))

                measures.append(f'site_status,agent_tok="tag-to-replace",user_name={user},url={url} status={status}i {time.time_ns()+ind}')

                print(measures)
                
            line_protocol = '\n'.join(measures) + '\n'
            
            with open('output.txt', "w") as file:
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
                response = requests.get(url, timeout=4)
                status_code = response.status_code
            except requests.exceptions.ConnectTimeout:
                status_code = 504
            except:
                status_code = 400
            data[id].append(status_code)
            
        self.save(data)
    
        return self.message

def main():
    agent = Agent()
    return agent.run()


if __name__ == "__main__":
    sys.exit(main())