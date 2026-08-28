from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pandas as pd

url = 'https://www.imdb.com/chart/top/'
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto(url)
#     page.wait_for_selector('ipc-metadata-list-summary-item')
#     html = page.content()
#     browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(3000)

    page.screenshot(path="debug.png", full_page=True)
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    browser.close()


