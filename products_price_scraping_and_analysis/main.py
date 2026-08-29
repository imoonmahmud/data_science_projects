import requests
from bs4 import BeautifulSoup
import re
import json

def get_product_links():
    url = 'https://www.rokomari.com/super-deal'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    containter = soup.find(class_='superdeal-products__container__grid')
    items = containter.find_all(class_='book-list-wrapper')
    with open('product_pages.txt', 'w', encoding='utf-8') as file:
        for item in items:
            file.write(f"https://www.rokomari.com/{item.find('a')['href']}\n")

def main(url):
    details = {}
    HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}

    product_page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(product_page.text, 'html.parser')

    details['title'] = soup.find('h1').get_text()
    details['price'] = soup.find(
        class_='superdeal-price-section__item-deal-price__text').get_text()
    details['overall_rating'] = f"{
        soup.find('h3').get_text()} out of 5 stars"

    # text = soup.find(class_='summary-text').get_text()
    # numbers = re.findall(r'\d+', text)
    # details['total_reviews'] = [int(num) for num in numbers][1]

    return details


if __name__ == '__main__':
    file = open('product_pages.txt', 'r')
    products_details = []
    for link in file.readlines():
        products_details.append(main(link))
    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(products_details, file, indent=4) 

