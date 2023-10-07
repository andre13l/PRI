import requests
import pandas as pd
from bs4 import BeautifulSoup
def scrap_books(pg):
    r=requests.get(f'https://www.amazon.in/gp/bestsellers/books/?pg='+str(pg))
    content=r.content
    soup=BeautifulSoup(content,'html.parser')
    alls = []
    for d in soup.findAll('div', attrs={'id':'gridItemRoot'} or {'class':'zg-more-list-types-container'}):    
        name = d.find('div', attrs={'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'})
        author = d.find('div', attrs={'class':'a-row a-size-small'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        users_rated = d.find('span', attrs={'class':'a-size-small'})
        site = d.find('a', attrs={'class':'a-link-normal', 'title': lambda x: x and x.endswith('out of 5 stars')})
        if site:
            href = site.get('href')
            product_id = href.split('/')[-3]
        else:
            href = ''
        #price = d.find('span', attrs={'class':'_cDEzb_p13n-sc-price_3mJ9Z'})
            
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
        '''if price is not None:
            all1.append(price.text)
        else:
            all1.append('0')'''
        all1.append(product_id)
        alls.append(all1)
    return alls

results = []
for i in range(1, 9):
    results.append(scrap_books(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book Name','Author','Rating','Customers_Rated','Href'])
df.to_csv('amazon_products.csv', index=False, encoding='utf-8')

df = pd.read_csv("amazon_products.csv")
df.shape
df.head(10)