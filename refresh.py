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