import urllib2
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

df = {'Language':[],'Tag_Count':[]}



def extract_tagged(url):
    #print('Extracting Content')
    content = urllib2.urlopen(url).read()
    soup = bs(content,'html.parser')
     
    for tag in soup.find_all('a',attrs={'class':'post-tag'}):
        df['Language'].append(tag.text)
    for count in soup.find_all('span',attrs={'class':'item-multiplier-count'}):
        df['Tag_Count'].append(count.text)
    
for i in range(1,3):
    extract_tagged('http://stackoverflow.com/tags?page='+str(i)+'&tab=popular')    
df['Tag_Count']=[int(i) for i in df['Tag_Count']]

df2= pd.DataFrame(df)
print(df2)


style.use('ggplot')

df2.sort_values(by=['Tag_Count'],ascending=False).head(10).set_index('Language').plot(kind='bar')
plt.show()

