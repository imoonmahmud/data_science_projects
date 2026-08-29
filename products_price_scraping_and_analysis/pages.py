import requests
from bs4 import BeautifulSoup
url = 'https://www.rokomari.com/super-deal'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'}

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

product_links = []

containter = soup.find(class_='superdeal-products__container__grid')
items = containter.find_all(class_='book-list-wrapper')
# with open('product_pages.txt', 'w', encoding='utf-8') as file:
#     for item in items:
#         file.write(f"https://www.rokomari.com/{item.find('a')['href']}\n")

for item in items:
    product_links.append(item.find('a')['href'])


