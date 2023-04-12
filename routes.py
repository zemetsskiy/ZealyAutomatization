import aiohttp

from config.params import get_cookies, get_header, get_quest_url, get_url_proxies, get_auth_proxies, profile_link, \
    GET_header


async def send_post_request(session, url, data, headers, cookies, proxy):
    proxy_url = get_url_proxies(proxy)
    username = get_auth_proxies(proxy)[0]
    password = get_auth_proxies(proxy)[1]
    proxy_auth = aiohttp.BasicAuth(username, password)

    async with session.post(url, data=data, headers=headers, cookies=cookies, proxy=proxy_url,
                            proxy_auth=proxy_auth) as resp:
        warn = ""
        data = await resp.json()
        if "error" in data:
            warn = data['error']['follow']
        elif "message" in data:
            warn = data['message'] + " or Already Claimed"
        return resp.status, warn


async def send_get_request(session, url, headers, cookies):
    async with session.get(url, headers=headers, cookies=cookies) as resp:
        response = await resp.json()
        return response


async def get_me(access_token):
    async with aiohttp.ClientSession() as session:
        result = await send_get_request(session, profile_link, GET_header, get_cookies(access_token))
        return result["discordHandle"]

