import requests
import pandas as pd
from bs4 import BeautifulSoup
def scrap_books(pg):
    r=requests.get(f'https://www.goodreads.com/list/show/2591.Best_Books_of_the_Decade_1830s?page='+str(pg))
    content=r.content
    soup=BeautifulSoup(content,'html.parser')
    alls = []
    for d in soup.findAll('td', attrs={'width':'100%'}):
        print(2)
        name = d.find('a', attrs={'class':'bookTitle'})
        author = d.find('a', attrs={'class':'authorName'})
        rating = d.find('span', attrs={'class':'minirating'})
        users_rated = d.find('span', attrs={'class':'minirating'})
        site = d.find('a', attrs={'class':'bookTitle'})
        
        if site:
            href = site.get('href')
            product_link = 'https://www.goodreads.com' + href
        else:
            href = ''
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
            all1.append(rating.text[1:4])
        else:
            all1.append('-1')
        if users_rated is not None:
            all1.append(users_rated.text[19:26])
        else:
            all1.append('0')
        all1.append(product_link)
        alls.append(all1)
    return alls

results = []
for i in range(1, 4):
    results.append(scrap_books(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book Name','Author','Rating','Customers_Rated','Href'])
df.to_csv('books.csv', index=False, encoding='utf-8')

df = pd.read_csv("books.csv")
df.shape
df.head(10)