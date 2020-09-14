import requests
from bs4 import BeautifulSoup
file_name = input('Write Your File Name: ')
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
'''file = open(file_name+'.txt','w')
file.write('Ny Times Titles \n\n')
for title in soup.find_all('h2','css-1vvhd4r e1voiwgp0'):
    file.write(str(title.text)+'\n')

file.close()'''

#or better programming practice


with open(file_name+'.txt','w') as file:
    file.write('Ny Times Titles \n\n')
    for title in soup.find_all('h2', 'css-1vvhd4r e1voiwgp0'):
        file.write(str(title.text)+'\n')