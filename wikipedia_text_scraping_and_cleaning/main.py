import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
headers = {
    'User-Agent': 'Mozilla/5.0'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
container = soup.find(id='mp-upper')
items = container.find_all(class_='mp-h2')
for item in items:
    print(item.get_text())