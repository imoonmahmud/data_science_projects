from playwright.sync_api import sync_playwright
import re
import json

def get_products():
    url = 'https://www.daraz.com.bd/catalog/?page=1&q=Keyboard'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
        page.goto(url)

        # wait for the container class to appear in the DOM
        page.wait_for_selector('._17mcb')

        container = page.query_selector('._17mcb')
        products = container.query_selector_all('._95X4G')

        with open('product_links.txt', 'w', encoding='utf-8') as file:
            for product in products:
                link = product.query_selector('a')
                if link:
                    href = link.get_attribute('href')
                    file.write(f"https:{href}\n")

def main(url):
    product_details = dict()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
        page.goto(url)

        page.wait_for_selector('.pdp-block__product-detail')
        product_detail = page.query_selector('.pdp-block__product-detail')

        try:
            title = product_detail.query_selector('h1').text_content().strip()
            product_details['title'] = title
        except AttributeError:
            product_details['title'] = 'NA'

        try:
            price = product_detail.query_selector('.pdp-price').text_content().replace('৳', '').strip()
            product_details['price'] = float(price.replace(',', ''))
        except AttributeError:
            product_details['price'] = 'NA'

        # scroll down to trigger lazy-loaded sections
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(1000)

        try:
            page.wait_for_selector('.mod-rating', timeout=3000)
            rating_detail = page.query_selector('.mod-rating')
            rating = rating_detail.query_selector('.score-average').text_content().strip()
            review_srt = rating_detail.query_selector('.count').text_content().strip()
            reviews = re.findall(r'\d+', review_srt)

            product_details.update({
                'rating': float(rating),
                'reviews': int(reviews[0])})
        except:
            product_details.update({
                'rating': 'NA',
                'reviews': 'NA'})

    return product_details


if __name__ == '__main__':
    get_products()
    file = open('product_links.txt', 'r')
    details = []

    for link in file.readlines():
        details.append(main(link))

    with open('product_details.json', 'w', encoding='utf') as file:
        json.dump(details, file, indent=4)