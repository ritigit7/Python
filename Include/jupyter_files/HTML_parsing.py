import requests 
from bs4 import BeautifulSoup 

URL = "https://www.vgmusic.com/music/console/nintendo/nes/"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

# f=open("link.txt",'w')
# for i in soup.find_all('a'):
#     print(i.get('href'))
#     f.write(i.get('href'))

for i in soup.find_all('table'):
    print(i)