import requests
import re

# Targeting a live, alternative stream service mirror node
TARGET_URL = "https://githubusercontent.com"
OUTPUT_FILE = "discovered_links.txt"

# Keywords configured to match name strings used by live streaming nodes
CHANNELS = ["ria", "prima", "citra", "ceria", "oasis", "arena", "bola", "showtime", "showcase", "daebak"]

def fetch_malay_streams():
    print("Connecting to live streaming data node...")
    try:
        response = requests.get(TARGET_URL, timeout=15)
        if response.status_code != 200:
            print("Target mirror node is offline.")
            return
            
        lines = response.text.split("\n")
        playlist_content = "#EXTM3U\n"
        found_count = 0
        
        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF"):
                line_lower = lines[i].lower()
                # Flexibly track matching entries across the stream manifest array
                if any(ch in line_lower for ch in CHANNELS):
                    if i + 1 < len(lines) and lines[i+1].strip().startswith("http"):
                        playlist_content += f"{lines[i]}\n{lines[i+1].strip()}\n"
                        found_count += 1
                        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(playlist_content)
            
        print(f"Extraction complete. Found {found_count} links.")
        
    except Exception as e:
        print("An error occurred during execution.")

if __name__ == "__main__":
    fetch_malay_streams()
