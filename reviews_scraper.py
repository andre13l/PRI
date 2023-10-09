import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrap_reviews(pg):
    r = requests.get(f'https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird')
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    alls = []
    
    for d in soup.findAll('article', attrs={'class':'ReviewCard'}):
        reviewer = d.find('div', attrs={'class':'ReviewerProfile__name'})
        rating = d.find('span', attrs={'class':'RatingStars RatingStars__small'})
        review = d.find('section', attrs={'class':'ReviewText'})
        date = d.find('span', attrs={'class':'Text Text__body3'})
        
        a=rating['aria-label']


        all1=[]
        if reviewer is not None:
            all1.append(reviewer.text)
        else:
            all1.append('unknown-reviewer')
        if a is not None:
            all1.append(str(a)[7:9])
        else:
            all1.append('-1')
        if review is not None:
            all1.append(review.text)
        else:
            all1.append('0')
        if date is not None:
            all1.append(date.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls

results = []

results.append(scrap_reviews(1))

flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Reviewer','Rating','Review','Date'])
df.to_csv('book_reviews.csv', index=False, encoding='utf-8')

df = pd.read_csv("book_reviews.csv")