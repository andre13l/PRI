import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrap_reviews(pg):
    r = requests.get(f'https://www.amazon.in/product-reviews/8119352947/ref=cm_cr_arp_d_paging_btm_next_2/261-5976745-5421030?pageNumber={pg}')
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    alls = []
    
    for d in soup.findAll('div', attrs={'class':'a-section celwidget'}):
        reviewer = d.find('span', attrs={'class':'a-profile-name'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        review = d.find('span', attrs={'data-hook':'review-body'})
        
        all1=[]
        if reviewer is not None:
            all1.append(reviewer.text)
        else:
            all1.append('unknown-reviewer')
        if rating is not None:
            all1.append(rating.text)
        else:
            all1.append('-1')
        if review is not None:
            all1.append(review.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls

results = []
for i in range(1, 4): # modify the range to scrape all the pages of reviews
    results.append(scrap_reviews(i))

flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Reviewer','Rating','Review'])
df.to_csv('book_reviews.csv', index=False, encoding='utf-8')

df = pd.read_csv("book_reviews.csv")
