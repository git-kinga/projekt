import requests
import json
from requests.auth import HTTPBasicAuth
# Grafana API endpoint
url = 'http://192.168.56.1:3000/api/dashboards/db'

login = 'admin'
password = 'admin'
auth=HTTPBasicAuth(login, password)
# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    
}

# Dashboard configuration
dashboard_config = {
    'dashboard': {
        'id': None,
        'title': 'Website Status',
        'panels': [
            {
                'type': 'graph',
                'title': 'HTTP Status Codes',
                'targets': []
            }
        ],
        'refresh': '5s'
    },
    'folderId': 0,
    'overwrite': False
}

# Convert the dashboard configuration to JSON
dashboard_payload = json.dumps(dashboard_config)

# Make the API request to create the dashboard
response = requests.post(url, headers=headers, data=dashboard_payload,auth=auth)

# Check the response status
if response.status_code == 200:
    print('Dashboard created successfully!')
else:
    print('Dashboard creation failed. Status code:', response.status_code)
    print('Error response:', response.text)
