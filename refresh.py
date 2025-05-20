import json
import requests
from datetime import datetime

def refresh_token(link):
    try:
        session = requests.Session()
        response = session.get(link, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            final_url = response.url
            if "token=" in final_url:
                return final_url
            else:
                print(f"No token found in: {final_url}")
                return None
        else:
            print(f"Bad status for {link}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_playlist():
    try:
        with open("channels.json", "r") as f:
            channels = json.load(f)
    except Exception as e:
        print("Error reading channels.json:", e)
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