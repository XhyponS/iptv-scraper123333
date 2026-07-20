import requests

# Put your exact protected playlist link inside the quotes below
TARGET_URL = "https://onm.rocket-ott.shop/n2hpXDJO3o/playlist.m3u"
OUTPUT_FILE = "discovered_links.txt"

def fetch_secured_playlist():
    print("Connecting to secure stream web...")
    
    # Passing specialized identity headers to trick the server into skipping the store redirect
    headers = {
        "User-Agent": "OTT-Navigator/1.7.6.1 (Linux; Android 11)",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    
    try:
        # The script passes the custom application header black alongside the web request
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"Server rejected request with status code: {response.status_code}")
            return

        playlist_text = response.text

        # Verify if we received valid playlist tracks or a web redirect text
        if "#EXTM3U" in playlist_text:
            # 1. Save the complete playlist file
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(playlist_text)
            
            # 2. Look through the text and extract individual streaming URLs
            print("\n--- Scanning Playlist for Streaming Links ---")
            link_count = 0
            for line in playlist_text.splitlines():
                if line.strip().startswith("http"):
                    print(f"Found streaming link: {line.strip()}")
                    link_count += 1
            
            if link_count == 0:
                print("No lines starting with 'http' were found inside the playlist.")
            print("----------------------------------------------\n")

            lines_count = len(playlist_text.split("\n"))
            print(f"Extraction successful! Saved {lines_count} lines into playlist file.")
        
        else:
            print("Warning: Received data layout, but it lacks playlist formatting parameters.")
            print("The server might be blocking the request or redirecting you. Response snippet:")
            print(playlist_text[:300]) # Prints the first 300 characters to help debug

    except Exception as e:
        print(f"An error occurred during execution: {e}")

# This trigger tells Python to run the function when you launch the file
if __name__ == "__main__":
    fetch_secured_playlist()
