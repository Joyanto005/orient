import os
import json
import time
import hashlib

def generate_token(url):
    # Simple token generator (mock) — বাস্তব টোকেন সিস্টেম জানলে সেটি বসাও
    now = int(time.time())
    valid_until = now + 3600
    dummy_key = "secret_key"
    token = hashlib.sha1(f"{url}{dummy_key}{now}".encode()).hexdigest()
    return f"{url}?token={token}-{valid_until}-{now}"

def main():
    with open("channels.json", "r") as f:
        channels = json.load(f)

    with open("output.m3u", "w") as out:
        out.write("#EXTM3U\n")
        for channel in channels:
            name = channel["name"]
            base_url = channel["url"]
            refreshed_url = generate_token(base_url)
            out.write(f"#EXTINF:-1,{name}\n{refreshed_url}\n")

if __name__ == "__main__":
    main()