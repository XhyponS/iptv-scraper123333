import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search  # Install via: pip install googlesearch-python

# A robust list of Google Dorks targeting open directories and text lists across the internet
DORK_QUERIES = [
  'filetype:m3u "extinf" "Astro Ria" OR "Astro Prima" OR "Astro Citra" OR "Astro Ceria" OR "Astro Oasis" "http"',
    'filetype:m3u "extinf" "Astro Arena" OR "Astro Bola" OR "Astro Showtime" OR "Astro Showcase" OR "Astro Daebak" "http"',
    'intitle:"index of" "m3u8" "Astro" OR "Bola 1" OR "Bola 2" OR "Arena 1" OR "Arena 2"',
    'inurl:playlist.m3u8 "Astro Ria" OR "Astro Prima" OR "Astro Citra" OR "Astro Ceria" OR "Astro Arena"'
]

def harvest_links():
    found_urls = []
    print("Initiating broad web search via Google Dorks...")
    
    for query in DORK_QUERIES:
        try:
            print(f"Searching for: {query}")
            # Crawling search engine results across the web
            for url in search(query, num_results=15, sleep_interval=5):
                found_urls.append(url)
        except Exception as e:
            print(f"Search engine rate-limit triggered: {e}")
            
    return list(set(found_urls))

def parse_and_validate(urls):
    valid_streams = []
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for url in urls:
        try:
            # If the discovered URL is a direct playlist, download it
            if url.endswith(('.m3u', '.m3u8')):
                res = requests.get(url, headers=headers, timeout=5)
                if "#EXTM3U" in res.text:
                    valid_streams.append(url)
        except:
            continue
            
    return valid_streams

if __name__ == "__main__":
    discovered_sources = harvest_links()
    verified_playlists = parse_and_validate(discovered_sources)
    
    # Save the harvested repositories to your folder structure
    with open("discovered_links.txt", "w") as f:
        for link in verified_playlists:
            f.write(f"{link}\n")
    print(f"Done. Discovered {len(verified_playlists)} open-web index links.")
