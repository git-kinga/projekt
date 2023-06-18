import requests
import time
import json

class Agent:
    def __init__(self):
        self.config_pull_url = "http://192.168.56.1:8000/api/config"
        # self.agent_id = input("Enter your agent ID: ")
        self.urls = []

    def get_config(self):
        response = requests.get(self.config_pull_url)
        print(response.text)
        if response.status_code == 200:
            self.urls=json.loads(response.text)
            return json.loads(response.text)
        else:
            return None

    def run(self):
        self.urls = self.get_config()
        data={}
        if self.urls is None:
            print("Error: Could not retrieve config")
            return
        for url in self.urls.values():
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            if response.status_code == 200:
                print(f"{url} returned a 200 OK response after {response_time:.2f} seconds")
            else:
                print(f"{url} returned a {response.status_code} response after {response_time:.2f} seconds")
            data[url]=response.status_code
        json_data=json.dumps(data)
        return json_data

def main():
    agent = Agent()
    print(agent.urls)
    json_data=agent.run()
    print(json_data)
    return json_data

if __name__ == "__main__":
    main()