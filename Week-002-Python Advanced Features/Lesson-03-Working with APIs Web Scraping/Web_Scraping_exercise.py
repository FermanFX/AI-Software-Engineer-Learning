import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
kitablar = soup.find_all("article", class_="product_pod")

print(f"{'Kitab Adı':<50} | {'Qiymət'}")
print("-" * 65)

for kitab in kitablar:
    ad = kitab.h3.a["title"]
    qiymet = kitab.find("p", class_="price_color").text
    print(f"{ad[:47] + 'veee' if len(ad) > 47 else ad:<50} | {qiymet}")
