import requests
from bs4 import BeautifulSoup

url_to_scrape = 'https://onm.rocket-ott.shop/n2hpXDJO3o/playlist.m3u'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36'
}

try:
    response = requests.get(url_to_scrape, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Your scraping logic here
except Exception as e:
    print(f"Error: {e}")
