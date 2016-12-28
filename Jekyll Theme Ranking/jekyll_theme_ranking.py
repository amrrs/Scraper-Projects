import urllib2
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
 

df = {'Theme Link':[],'Stars':[]}

#print(content)

def extract_star(url):
    #print('Extracting Content')
    content = urllib2.urlopen(url).read()
    soup = bs(content,'html.parser')
    #counts = []
    for count in soup.findAll('a',class_=re.compile('social-count'),href=re.compile('star')):
        return count.text
mainContent = urllib2.urlopen('https://github.com/jekyll/jekyll/wiki/Themes').read()
soup = bs(mainContent,'html.parser')
i = 0
for link in soup.findAll('a',href=re.compile('github'), text='source'):
    df['Theme Link'].append(link['href'])
    df['Stars'].append(float(extract_star(link['href']).replace(',', '')))
    #i = i + 1
    #if i > 5:
    #    break
    #print(df)
pd_df = pd.DataFrame(df)


print(pd_df.sort_values(by=['Stars'],ascending=False).head(10))
       
