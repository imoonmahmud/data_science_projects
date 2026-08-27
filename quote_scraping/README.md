# Quote Guessing Game using Web Scraping in Python

In the command-line game that scrapes quotes from from a website and challenges the user to guess the author.

## Features

* Scrape quotes from multiple pages
* Randomly selects a quote from the dictionary created
* Give the user 4 guesses
* Keep giving hints until either number of chances reach zero or the user gets it right
* Write message for success and failure
* Give the correct answer when all guesses are used

## Requirements

* Python 3.x
* `requests`
* `beautifulsoup4`


## Example

```text
==== Quote ====
“The world as we have created it is a process of our thinking.”

Who said the quote? Guesses remaining 4: Albert Einstein

CONGRATULATIONS!!! YOU GOT IT RIGHT
```

## Project Structure

```text
quote-guessing-game/
│
├── main.py
└── README.md
```

## Data Source

Quotes and author information are collected from:

**Quotes to Scrape** — `quotes.toscrape.com`

## Note

This project is intended for learning purposes, particularly practicing:

* Web scraping
* HTML parsing
* HTTP requests
* Basic game logic