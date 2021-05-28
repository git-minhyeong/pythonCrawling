import requests

naver_data = {'sm' : 'top_hty',
            'fbm' : 1,
            'ie' : 'utf8',
            'query' : '검색' }

r = requests.get('https://search.naver.com/search.naver', params=naver_data)
r.url