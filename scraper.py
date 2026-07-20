import requests
import re

# Directly targeting an alternative open-source repository that aggregates live streams
TARGET_URL = "https://githubusercontent.com"
OUTPUT_FILE = "discovered_links.txt"

# Your specific track keys to extract cleanly
CHANNELS = ["ria", "prima", "citra", "ceria", "oasis", "arena", "bola", "showtime", "showcase", "daebak"]

def fetch_malay_streams():
    print("Connecting to live streaming data node...")
    try:
        response = requests.get(TARGET_URL, timeout=15)
        if response.status_code != 200:
            print("Target mirror node is currently offline.")
            return
            
        lines = response.text.split("\n")
        playlist_content = "#EXTM3U\n"
        found_count = 0
        
        # Step through the playlist arrays systematically
        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF"):
                line_lower = lines[i].lower()
                
                # Check for matches against your Astro targets
                if any(ch in line_lower for ch in CHANNELS):
                    if i + 1 < len(lines) and lines[i+1].startswith("http"):
                        playlist_content += f"{lines[i]}\n{lines[i+1]}\n"
                        found_count += 1
                        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(playlist_content)
            
        print(f"Extraction successful. Generated {found_count} clean streaming tracks.")
        
    except Exception as e:
        print(f"A processing routine error occurred: {e}")

if __name__ == "__main__":
    fetch_malay_streams()                    playlist_content += f"\n# From source: {url}\n{res.text}\n"
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
