import requests
import pandas as pd
from bs4 import BeautifulSoup

'''results = []
for i in range(1, page + 1):
    results.append(fetch_books(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book Name'])
df.to_csv('amazon_products.csv', index=False, encoding='utf-8')

df = pd.read_csv("amazon_products.csv")

df.head(10)'''

r=requests.get(f'https://www.amazon.in/gp/bestsellers/books/?pg=1')
content=r.content
soup=BeautifulSoup(content,'html.parser')
alls = []
for d in soup.find_all('div', attrs={'id':'gridItemRoot'}):    
    name = d.find('a', attrs={'class':'a-link-normal'})
    author = d.find('div', attrs={'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'})
    rating = d.find('span', attrs={'class':'a-icon-alt'})
    users_rated = d.find('span', attrs={'class':'a-size-small'})
    price = d.find('span', attrs={'class':'_cDEzb_p13n-sc-price_3mJ9Z'})
        
    all1=[]
    if name is not None:
        all1.append(name.text)
    else:
        all1.append("unknown-product")
    if author is not None:
        all1.append(author.text)
    else:    
        all1.append('0')
    if rating is not None:
        all1.append(rating.text)
    else:
        all1.append('-1')
    if users_rated is not None:
        all1.append(users_rated.text)
    else:
        all1.append('0')
    if price is not None:
        all1.append(price.text)
    else:
        all1.append('0')
    alls.append(all1)

print(alls)