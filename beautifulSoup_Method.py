from bs4 import BeautifulSoup

soup.title
## 문서의 tltle 태그의 상부를 출력
## <title> The Dormouse's story</title>

soup.title.name
## title 태그의 이름을 출력
## 'title'

soup.title.string
## tltle 태그가 가지고 있는 내용을 출력
## "The Dormouse's story"

soup.p
## 문서의 p 태그 정보 출력
## <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
## p 태그가 가지고 있는 class 출력
## ['title]

soup.a
## a 태그의 정보를 출력
## <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
## 문서에서 a 태그가 하나가 아니기 때문에 전체를 탐색하기 위해서 find_all() 사용
## <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
## <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
## <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> 

soup.find(id="link3")
## id가 link3 라는 것만 출력
## <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>