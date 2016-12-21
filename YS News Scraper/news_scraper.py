import urllib, urllib2
from bs4 import BeautifulSoup, Comment

url='https://yourstory.com/news/'
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

site_name = soup.find("meta",  property="og:site_name")
title = soup.find("meta",  property="og:title")
desc = soup.find("meta",  property="og:description")

for i in range(0,2): print '**'*50

print(site_name["content"] if title else "No meta site name given")
print(title["content"] if url else "No meta title given")
print(desc["content"] if url else "No meta desc given")

for i in range(0,3): print '**'*50

for i,row in enumerate(soup.find_all('div',attrs={"class" : "title-small"})):
    if i > 9:
        break
    print str(i+1)+' '+row.text.strip()    
    print '-'*(len(row.text.strip())/3)
    
for i in range(0,3): print '**'*50
