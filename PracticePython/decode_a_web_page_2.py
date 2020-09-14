import requests
from bs4 import BeautifulSoup

URL = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(URL)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
for source in soup.find_all('p'):
    print(source.text)