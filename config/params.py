def get_cookies(access_token):
    return {
        'subdomain': 'suiswap-app',
        'access_token': access_token,
        'cookie-config': '{%22functional%22:true%2C%22analytics%22:true%2C%22marketing%22:true}',
    }


def get_url_proxies(proxy):
    split_proxy = proxy.split(":")
    proxy_url = split_proxy[0] + ':' + split_proxy[1]
    return f"http://{proxy_url}"  # 'socks5://your-proxy-server:port'


def get_auth_proxies(proxy):
    split_proxy = proxy.split(":")
    proxy_auth = [split_proxy[2],  split_proxy[3]]
    return proxy_auth


def parse_tokens(file_path):
    token_to_proxies = {}
    with open(file_path, 'r') as f:
        for line in f:
            token, proxy = line.strip().split()
            token_to_proxies[token] = proxy
    return token_to_proxies

profile_link = "https://api.zealy.io/communities/suiswap-app/users/me"

GET_header = {
    'authority': 'api.zealy.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru',
    # 'cookie': '_ga=GA1.1.349002535.1681232021; ajs_anonymous_id=b777a28e-1aa8-4d39-9a3e-fda3d9e35a00; connect.sid=s%3AeZVSC1DucTtF0h3cGfR5a8xxwL5X8j2U.0x6cRNBmj7ViPlbpyGMlTZZDSCh3yjxEeKQm5Uww%2FTk; subdomain=suiswap-app; cookie-config={%22functional%22:true%2C%22analytics%22:true%2C%22marketing%22:true}; access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJkNGIxMTZjMS0zZmMxLTRmYTMtYmQ4NS04MzI4OTk5YzM4YzUiLCJhY2NvdW50VHlwZSI6ImRpc2NvcmQiLCJpYXQiOjE2ODEyMzIxMjUsImV4cCI6MTY4MzgyNDEyNX0.vv-7l-uFBM0UrT1fjut7Q8dkSmqgW3EgnvGX0HgonP0; ajs_user_id=d4b116c1-3fc1-4fa3-bd85-8328999c38c5; analytics_session_id=1681284895299; crisp-client%2Fsession%2F0fc84ec9-c5b0-4a18-8c4a-b7bc63bd6573=session_fb4b0816-29a2-4412-b1d6-bc4fcd7bf93f; analytics_session_id.last_access=1681289506999; _ga_KHH93XWSWL=GS1.1.1681286878.6.1.1681289510.0.0.0',
    'if-none-match': 'W/"7c2-fZOProLPhfc+1mwL8wdXhCFhqdM"',
    'origin': 'https://zealy.io',
    'referer': 'https://zealy.io/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def get_header(boundary):
    return {
        'authority': 'api.zealy.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'multipart/form-data;' + f' boundary={boundary}',
        'origin': 'https://zealy.io',
        'referer': 'https://zealy.io/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }


def get_quest_url(quest_id):
    return f'https://api.zealy.io/communities/suiswap-app/quests/{quest_id}/claim'


def main():
    parse_tokens("tokens.txt")


if __name__ == "__main__":
    main()
