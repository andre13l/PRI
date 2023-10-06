import requests

from bs4 import BeautifulSoup

def fetch_reviews():
    url = 'https://www.yelp.com/biz/la-crosta-woodfire-pizzeria-los-angeles-2?osq=La+Crosta+Woodfire+Pizzeria'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all('div', {'class': 'review-content'})
    for review in reviews:
        print(review.find('p').text)

fetch_reviews()