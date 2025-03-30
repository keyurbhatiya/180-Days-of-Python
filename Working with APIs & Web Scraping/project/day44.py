# Day 44: Practice Project (News Scraper)

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    news_articles = soup.find_all("article")

    for article in news_articles:
        title = article.find("h2").text
        summary = article.find("p").text
        link = article.find("a")["href"]

        print(f"Title: {title}")
        print(f"Summary: {summary}")
        print(f"Link: {link}")
        print("---")
else:
    print("Error:", response.status_code)

