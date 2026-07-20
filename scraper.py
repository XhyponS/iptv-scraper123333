import requests

# Put your exact protected playlist link inside the quotes below
TARGET_URL = "https://onm.rocket-ott.shop/n2hpXDJO3o/playlist.m3u"
OUTPUT_FILE = "discovered_links.txt"

def fetch_secured_playlist():
    print("Connecting to secure stream node...")
    
    # Passing specialized identity headers to trick the server into skipping the store redirect
    headers = {
        "User-Agent": "OTT-Navigator/1.7.4.1 (Linux; Android 11)",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    
    try:
        # The script passes the custom application header block alongside the web request
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"Server rejected request with status code: {response.status_code}")
            return
            
        playlist_text = response.text
        
        # Verify if we received valid playlist tracks or a web redirect text
        if "#EXTM3U" in playlist_text:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(playlist_text)
            lines_count = len(playlist_text.split("\n"))
            print(f"Extraction successful! Saved {lines_count} lines into playlist file.")
        else:
            print("Warning: Received data layout, but it lacks playlist formatting parameters.")
            
    except Exception as e:
        print(f"A processing network routine error occurred: {e}")

if __name__ == "__main__":
    fetch_secured_playlist()
