import requests

r = requests.get('http://solotodo.com/', allow_redirects=False)
print(r.status_code)
