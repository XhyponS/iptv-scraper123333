import requests

# The main active global index stream file node
REGIONAL_PLAYLIST_URL = "https://github.io"
OUTPUT_FILE = "discovered_links.txt"

# Your specific list of target channels
ASTRO_CHANNELS = [
    "astro ria", "astro prima", "astro citra", "astro ceria", 
    "astro oasis", "astro arena", "astro bola", "bola 1", "bola 2", 
    "arena 1", "arena 2", "astro showtime", "astro showcase", "astro daebak"
]

def build_playlist():
    print("Fetching direct global open data streams...")
    try:
        response = requests.get(REGIONAL_PLAYLIST_URL, timeout=15)
        if response.status_code != 200:
            print("Target data stream server node is currently unreachable.")
            return
            
        lines = response.text.split("\n")
        playlist_content = "#EXTM3U\n"
        found_count = 0
        
        # Parse the dataset step-by-step
        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF"):
                line_lower = lines[i].lower()
                # Check if ANY of your specified Astro channels match this specific track line
                match_found = any(channel in line_lower for channel in ASTRO_CHANNELS)
                
                if match_found:
                    if i + 1 < len(lines) and lines[i+1].startswith("http"):
                        playlist_content += f"{lines[i]}\n{lines[i+1]}\n"
                        found_count += 1
                        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(playlist_content)
            
        print(f"Transfer complete. Generated {found_count} Astro stream entries successfully.")
        
    except Exception as e:
        print(f"Network error during script parsing loop: {e}")

if __name__ == "__main__":
    build_playlist()
