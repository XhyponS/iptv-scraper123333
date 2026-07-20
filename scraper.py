import requests

# This script bypasses search engine constraints by grabbing the entire curated Malaysia data stream cluster
REGIONAL_PLAYLIST_URL = "https://githubusercontent.com"
OUTPUT_FILE = "discovered_links.txt"

def build_playlist():
    print("Fetching direct regional open data streams...")
    try:
        response = requests.get(REGIONAL_PLAYLIST_URL, timeout=15)
        if response.status_code != 200:
            print("Target regional server node is currently unreachable.")
            return
            
        # The database stream content is already formatted correctly as an M3U file
        playlist_data = response.text
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(playlist_data)
            
        lines_count = len(playlist_data.split("\n"))
        print(f"Transfer complete. Generated structural stream entries successfully.")
        
    except Exception as e:
        print(f"Network error during script parsing loop: {e}")

if __name__ == "__main__":
    build_playlist()
