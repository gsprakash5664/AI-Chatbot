# google_search.py
import requests

def google_search(query):
    api_key = "AIzaSyC2EyQzmIjpxsvKbODWt9cbrznhGQRnUVE"         # ← Paste your API key here
    cse_id = "7302209bf11b54faa"        # ← Paste your Search Engine ID here

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    results = response.json()
    if "items" in results:
        return results["items"][0]["snippet"]
    else:
        return "Sorry, no results found."
