import requests
from bs4 import BeautifulSoup

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)

if response.status_code == 200:
    comments = response.json()
    emails = [comment['email'] for comment in comments]
    print("Extracted Emails:", emails[:10]) # Displaying first 10 for brevity

url1 = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url1)
if response.status_code == 200:
    users = response.json()
    for user in users:
        name = user['name']
        email = user['email']
        city = user['address']['city']
        print(f"Name: {name} | Email: {email} | City: {city}")

url2="http://books.toscrape.com/"
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')
print("Books under £50:")
for book in books:
    title = book.h3.a['title']
    
    price_text = book.find('p', class_='price_color').text
    price = float(price_text.split('£')[-1])
    
    if price < 50.00:
        print(f"- {title}: £{price}")