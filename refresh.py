import json
import requests
from datetime import datetime

def refresh_token(link):
    try:
        response = requests.get(link, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            return response.url  # Updated tokenized link
        else:
            return None
    except Exception as e:
        print(f"Error refreshing token for {link}: {e}")
        return None

def update_playlist():
    try:
        with open("channels.json", "r") as f:
            channels = json.load(f)
    except Exception as e:
        print("Error loading channels.json:", e)
        return

    playlist = "#EXTM3U\n"

    for ch in channels:
        new_link = refresh_token(ch["url"])
        if new_link:
            playlist += f'#EXTINF:-1,{ch["name"]}\n{new_link}\n'
        else:
            playlist += f'#EXTINF:-1,{ch["name"]} (OFFLINE)\n{ch["url"]}\n'

    with open("output.m3u", "w") as f:
        f.write(playlist)

    print(f"Updated at {datetime.now()}")

# NOTE: এটা Flask থেকে কল হবে, তাই সরাসরি রান না করলেও চলবে