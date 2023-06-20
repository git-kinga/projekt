import requests

url = 'http://localhost:8000/api/config/user01'

token = 'wGWAGew4DUGaxPQGt5x5bBhfKRjFbsaM'

req = requests.post(url, headers={'Authorization' : token})
print(req.text)