import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='g'):
            link = g.find('a', href=True)
            if link:
                results.append(link['href'])
        return results
    else:
        print("Failed to retrieve search results.")
        return []

search_query = 'site:pastebin.com "astro" "iptv"'
results = google_search(search_query)
for url in results:
    print(url)                if line.strip().startswith("http"):
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
