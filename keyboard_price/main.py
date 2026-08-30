from playwright.sync_api import sync_playwright

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

        with open('products_links.txt', 'w', encoding='utf-8') as file:
            for product in products:
                link = product.query_selector('a')
                if link:
                    href = link.get_attribute('href')
                    file.write(f"{href}\n")
