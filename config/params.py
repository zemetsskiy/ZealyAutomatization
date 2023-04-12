def get_cookies(access_token):
    return {
        'subdomain': 'suiswap-app',
        'access_token': access_token,
        'cookie-config': '{%22functional%22:true%2C%22analytics%22:true%2C%22marketing%22:true}',
    }


def get_url_proxies(proxy):
    split_proxy = proxy.split(":")
    proxy_url = split_proxy[0] + ':' + split_proxy[1] + ':' + split_proxy[2]
    return proxy_url  # 'socks5://your-proxy-server:port'


def get_auth_proxies(proxy):
    split_proxy = proxy.split(":")
    proxy_auth = [split_proxy[3],  split_proxy[4]]
    return proxy_auth


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
