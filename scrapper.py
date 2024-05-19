import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime
import requests

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_quotes(page):
    url = f"https://www.goodreads.com/quotes?page={page}"
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        quotes_divs = soup.find_all('div', {'class': 'quoteText'})
        quotes = []
        for quote_div in quotes_divs:
            quote_text = quote_div.text.strip().split("\n")[0]
            author = quote_div.find_next('span', {'class': 'authorOrTitle'}).text.strip()
            tags = [tag.text for tag in quote_div.find_next('div', {'class': 'greyText'}).find_all('a')]
            quotes.append({
                "quote": quote_text,
                "author": author,
                "tags": tags,
                "date": datetime.utcnow().isoformat()
            })
        return quotes

async def store_data(quotes):
    for quote in quotes:
        requests.post('http://localhost:5000/store', json=quote)

async def main():
    try:
        for page in range(1, 6):  # Change this range to scrape more or fewer pages
            quotes = await scrape_quotes(page)
            await store_data(quotes)
    except Exception as e:
        print(f"An error occurred or other services are not running: {e}")

if __name__ == '__main__':
    asyncio.run(main())