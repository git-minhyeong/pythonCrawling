import requests

with requests.Session() as s:
    s.headers.update({'user-agent' :
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"})

    r = s.get('http://naver.com')
    r = s.get('http://daum.net')