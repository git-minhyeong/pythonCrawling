import requests

r = requests.get('https://api.github.com/events')

payload = {'key1' : 'value1', 'key2' : 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
r.status_code
r.url