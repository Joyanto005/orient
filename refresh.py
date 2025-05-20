import json
import requests
from datetime import datetime

def refresh_token(link):
    try:
        # আগের token বাদ দিয়ে নতুন redirect URL পাই
        response = requests.get(link, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return response.url
        else:
            return None
    except:
        return None

def update_playlist():
    with open("channels.json", "r") as f:
        channels = json.load(f)

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

if __name__ == "__main__":
    update_playlist()