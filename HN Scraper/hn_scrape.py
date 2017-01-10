import urllib2
from bs4 import BeautifulSoup as bs


def extract_news(url):
    print('HN Top Stories:\n'+'-'*50+'\n'+'-'*50)
    content = urllib2.urlopen(url).read()
    soup = bs(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        print(str(i+1)+' :: '+tag.text + '\n' + '-'*51) if tag.text!='More' else ''
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    print('End') 
    
extract_news('https://news.ycombinator.com/')    
 

 
