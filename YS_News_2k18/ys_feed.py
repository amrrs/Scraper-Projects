import requests
from bs4 import BeautifulSoup
url='https://yourstory.com/feed'
content = requests.get(url).content
soup = BeautifulSoup(content, "html.parser")
for n,t in enumerate(soup.findAll("title")):
    print(str(n) + " - "+ t.text)
