import requests
from requests.models import Response

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = 'http://www.useragentstring.com/'

r = requests.get(url, headers = header)

Response.text