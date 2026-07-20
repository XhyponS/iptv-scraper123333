import requests

# 1. Target Channels List (Must match naming conventions in global databases)
TARGET_CHANNELS = [
    "Astro Ria", "Astro Prima", "Astro Citra", "Astro Ceria", 
    "Astro Oasis", "Astro Arena", "Astro Bola", "Astro Showtime", 
    "Astro Showcase", "Astro Daebak", "Bola 1", "Bola 2", 
    "Arena 1", "Arena 2"
]

# 2. Source database (Using the massive, community-updated iptv-org index)
SOURCE_URL = "https://github.io"
OUTPUT_FILE = "discovered_links.txt"

def harvest_channels():
    print("Downloading global streaming index database...")
    try:
        response = requests.get(SOURCE_URL, timeout=15)
        if response.status_code != 200:
            print("Failed to download database node.")
            return
            
        lines = response.text.split("\n")
        playlist_content = "#EXTM3U\n"
        found_count = 0
        
        # 3. Parse and filter specifically for your Astro channels
        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF"):
                # Check if any of your requested channels are on this track line
                for channel in TARGET_CHANNELS:
                    if channel.lower() in lines[i].lower():
                        # Grab the next line which contains the streaming URL
                        if i + 1 < len(lines) and lines[i+1].startswith("http"):
                            playlist_content += f"{lines[i]}\n{lines[i+1]}\n"
                            found_count += 1
                            break
                            
        # 4. Save parsed results
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(playlist_content)
            
        print(f"Success! Filtered and saved {found_count} active stream pathways.")
        
    except Exception as e:
        print(f"An execution error occurred: {e}")

if __name__ == "__main__":
    harvest_channels()
