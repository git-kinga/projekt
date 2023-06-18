import requests
import json
from requests.auth import HTTPBasicAuth

login = 'admin'
password = 'admin'
auth=HTTPBasicAuth(login, password)

# Define the Grafana API endpoint and headers
api_url = 'http://192.168.56.1:3000/api/datasources'
headers = {
    'Content-Type': 'application/json',
}

# Cinfigure the InfluxDB data source
data_source_config = {
    'name': 'InfluxDB',
    'type': 'influxdb',
    'url': 'http://192.168.56.1:8086',
    'access': 'proxy',
    'database': 'mydb',
    'user': 'admin',
    'password': 'admin',
    'basicAuth': False,
    'isDefault': True
}

# Send the API request to create the data source
response = requests.post(api_url, headers=headers, data=json.dumps(data_source_config), auth=auth)

# Check the response status code
if response.status_code == 200:
    print('InfluxDB data source created successfully.')
    print('Response:', response.text)
else:
    print('Failed to create InfluxDB data source. Status code:', response.status_code)
    print('Response:', response.text)

# Dashboard creation
