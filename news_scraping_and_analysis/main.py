import newspaper
import feedparser
import json

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        article = newspaper.Article(entry.link)
        article.download()
        article.parse()
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publist_date': article.publish_date,
            'content': article.text
        })
    return articles


feed_url = 'https://feeds.bbci.co.uk/news/rss.xml'
with open('news.json', 'w', encoding='utf-8') as file:
    json.dump(scrape_news_from_feed(feed_url), file, indent=4)