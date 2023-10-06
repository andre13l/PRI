import requests
from bs4 import BeautifulSoup

def fetch_reviews():
    url = 'https://www.yelp.pt/biz/le-grand-los-angeles-3'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the reviews container is present
        reviews = soup.find_all('div', {'class': 'review-content'})
        if reviews:
            for review in reviews:
                # Check if the review text is present
                review_text = review.find('p')
                if review_text:
                    print(review_text.text)
                else:
                    print("No review text found in a review.")
        else:
            print("No reviews found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Call the function
fetch_reviews()
