import time
import requests
from googlesearch import search

# Customized queries targeting unprotected text dumps and playlists across the open web
DORK_QUERIES = [
    'filetype:m3u "extinf" "Astro Ria" OR "Astro Prima" OR "Astro Citra"',
    'intitle:"index of" "m3u8" "Astro" OR "Bola" OR "Arena"',
    'inurl:playlist.m3u8 "Astro Ria" OR "Astro Ceria"',
    '"#EXTINF" "Astro Arena" "http"'
]

OUTPUT_FILE = "discovered_links.txt"

def harvest_web_links():
    found_urls = []
    print("Initiating custom internet harvesting pass...")
    
    # 1. Query public search indexes for active configurations
    for query in DORK_QUERIES:
        try:
            print(f"Searching index for: {query}")
            for url in search(query, num_results=10, sleep_interval=10):
                found_urls.append(url)
        except Exception as e:
            print(f"Search engine delay triggered: {e}")
            
    playlist_content = "#EXTM3U\n"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # 2. Extract content logs from found targets
    for url in list(set(found_urls)):
        try:
            if not url.endswith(('.html', '.htm')):
                res = requests.get(url, headers=headers, timeout=5)
                if "#EXTM3U" in res.text or "http" in res.text:
                    playlist_content += f"\n# From source: {url}\n{res.text}\n"
        except:
            continue
            
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(playlist_content)
    print("Harvest complete.")

if __name__ == "__main__":
    harvest_web_links()                    playlist_content += f"\n# From source: {url}\n{res.text}\n"
        except:
            continue
            
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(playlist_content)
    print("Harvest complete.")

if __name__ == "__main__":
    harvest_web_links()
