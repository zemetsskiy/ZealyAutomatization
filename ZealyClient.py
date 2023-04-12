import asyncio
import time
import logging
import aiohttp

from aiohttp_socks import ProxyConnector, ProxyType

from config.quests import quests
from config.params import get_cookies, get_header, get_quest_url, get_url_proxies, get_auth_proxies
from config.tokens import access_to_account

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


async def send_post_request(session, url, data, headers, cookies, proxy):
    proxy_url = get_url_proxies(proxy)

    username = get_auth_proxies(proxy)[0]
    password = get_auth_proxies(proxy)[1]

    logger.info(f"Proxy connect: {proxy_url}, Auth: {username}--{password} ")

    proxy_auth = aiohttp.BasicAuth(username, password)
    async with session.post(url, data=data, headers=headers, cookies=cookies, proxy=proxy_url, proxy_auth=proxy_auth) as resp:
        result = resp.status

        #TODO add try exception
        data = await resp.json()
        ip_address = 0
        return [result, ip_address]


class ZealyClient:
    # claim link ex: https://api.zealy.io/communities/suiswap-app/quests/b7c3412f-c534-45dc-baf7-fbaee7fdd085/claim
    def __init__(self):
        self.base_url = "https://api.zealy.io/communities/suiswap-app/quests"

    def claim_onboarding(self):
        pass

    @staticmethod
    async def claim_special():
        for acc_token, acc_proxy in access_to_account.items():
            async with aiohttp.ClientSession() as session:
                for key, data in quests["special"].items():
                    result = await send_post_request(session,
                                                     get_quest_url(key),
                                                     data,
                                                     get_header(data[2:40]),
                                                     get_cookies(acc_token),
                                                     acc_proxy)
                    # print(get_quest_url(key))
                    logger.info(f'Response {key[0:4]}:  STATUS CODE {result[0]}')
                    time.sleep(2)

    # @staticmethod
    # async def claim_quiz():
    #     async with aiohttp.ClientSession() as session:
    #         for key, data in quests["quiz"].items():
    #             result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
    #             print(f'Response {key[0:4]}: {result}')

    def claim_boost(self):
        pass

    def claim_join(self):
        pass

    def claim_twitter(self):
        pass

    # @staticmethod
    # async def claim_partner_twitter():
    #     async with aiohttp.ClientSession() as session:
    #         for key, data in quests["partner_twitter"].items():
    #             result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
    #             print(f'Response {key[0:4]}: {result}')

    # @staticmethod
    # async def claim_suiswap_friend():
    #     async with aiohttp.ClientSession() as session:
    #         for key, data in quests["suiswap_friend"].items():
    #             result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
    #             print(f'Response {key[0:4]}: {result}')

    # TODO Получать XP каждого клиента


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ZealyClient.claim_special())


if __name__ == "__main__":
    main()
    # proxy = 'http://178.211.149.180:62908:zFsbxPgX:FrXv1qhd'
    # print(get_url_proxies(proxy))
    # print(get_auth_proxies(proxy)[0], get_auth_proxies(proxy)[1])
