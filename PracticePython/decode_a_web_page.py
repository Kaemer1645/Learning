import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
for title in soup.find_all('h2','css-1vvhd4r e1voiwgp0'):
    print(title.text)




