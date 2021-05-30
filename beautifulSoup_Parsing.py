from bs4 import BeautifulSoup
soup = BeautifulSoup(parseExampleHtml_doc, 'html.parser')

print(soup.prettify())