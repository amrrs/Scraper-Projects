import urllib, urllib2
from bs4 import BeautifulSoup, Comment
import pandas as pd
import re
import matplotlib.pyplot as plt

url='https://indianbloggers.org/'
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

#initalizing an empty dictionary that would be written as Pandas Dataframe and then CSV
d = {'title':[],'links':[]}

#initializing blog hosting category
cat = {'blogspot':0,'wordpress':0,'others':0}

for link in soup.find_all('a',):
    if len(link.text.strip()) > 1 and bool(re.match('^http',link['href'])) and not bool(re.search('indianbloggers|twitter|facebook',link['href'])):
        d['title'].append(link.text)
        d['links'].append(link['href'])
        #finding the blog hosting type
        if re.search('blogspot',link['href']):
            cat['blogspot']+=1
        elif re.search('wordpress',link['href']):
            cat['wordpress']+=1
        else:
            cat['others']+=1
        #d['len'].append(len(link.text.strip()))
    
blog_list = pd.DataFrame(d).set_index('title')

blog_list.to_csv('blog_list.csv', encoding='utf-8')

print(str(len(blog_list.index))+' rows written')

print(cat)

#plotting the blog hosting type 

plt.bar(range(len(cat)), cat.values(), align='center')
plt.xticks(range(len(cat)), cat.keys())

plt.show()
