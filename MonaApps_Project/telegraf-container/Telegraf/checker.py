import requests
import time
import json

class Agent:
    def __init__(self):
        self.config_pull_url = "http://host.docker.internal:8000/api/config/"
        # self.agent_id = input("Enter your agent ID: ")
        self.urls = []
        print('Init')

    def get_config(self):
        print('Get_config')
        response = requests.get(self.config_pull_url)
        print(response.text)
        if response.status_code == 200:
            self.urls=json.loads(response.text)
            return json.loads(response.text)
        else:
            return None

    def save(self, data):
        line_protocol = '\n'.join([f'site_status,users_tag="tag-to-replace" url="{url}",status="{status}" {time.time_ns()+ind}' 
                                   for ind, (url, status) in enumerate(data.items())])
        
        with open('/app/output.txt', "w") as file:
            file.write(line_protocol)
        return True
        
    def run(self):
        self.urls = self.get_config()
        data={}
        if self.urls is None:
            print("Error: Could not retrieve config")
            return
        for url in self.urls.values():
            url = url if url.startswith('http') else 'https://' + url
            start_time = time.time()
            try:
                response = requests.get(url)
                response_time = time.time() - start_time
                if response.status_code == 200:
                    print(f"{url} returned a 200 OK response after {response_time:.2f} seconds")
                    data[url]=response.status_code
                else:
                    print(f"{url} returned a {response.status_code} response after {response_time:.2f} seconds")
                    data[url]=response.status_code
            except:
                print(f"{url} Failed to establish a new connection")
                data[url]='error'
        json_data=json.dumps(data)
        if self.save(data):
            print("Data saved")
        return json_data

def main():
    agent = Agent()
    json_data=agent.run()
    print(json_data)
    return True

if __name__ == "__main__":
    main()
    