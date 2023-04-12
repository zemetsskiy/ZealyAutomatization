import asyncio
import time
import aiohttp

from config.quests import quests
from config.params import get_cookies, get_header, get_quest_url,  profile_link, GET_header
from config.tokens import token_to_proxies
from config.logger import logger
from config.tweet_links import tweet_links
from routes import send_post_request, send_get_request, get_me


class ZealyClient:
    # claim link ex: https://api.zealy.io/communities/suiswap-app/quests/b7c3412f-c534-45dc-baf7-fbaee7fdd085/claim
    def __init__(self):
        self.base_url = "https://api.zealy.io/communities/suiswap-app/quests"

    @staticmethod
    async def claim_onboarding():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["onboarding"].items():
                        resp, warn = await send_post_request(session,
                                                             get_quest_url(key),
                                                             data,
                                                             get_header(data[2:40]),
                                                             get_cookies(acc_token),
                                                             acc_proxy)
                        if resp == 200:
                            logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                        elif resp == 400:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')
                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_special():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["special"].items():
                        resp, warn = await send_post_request(session,
                                                             get_quest_url(key),
                                                             data,
                                                             get_header(data[2:40]),
                                                             get_cookies(acc_token),
                                                             acc_proxy)
                        if resp == 200:
                            logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                        elif resp == 400:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')
                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_quiz():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["quiz"].items():
                        resp, warn = await send_post_request(session,
                                                             get_quest_url(key),
                                                             data,
                                                             get_header(data[2:40]),
                                                             get_cookies(acc_token),
                                                             acc_proxy)
                        if resp == 200:
                            logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                        elif resp == 400:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')
                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_boost():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["boost"].items():
                        if data != "":
                            resp, warn = await send_post_request(session,
                                                                 get_quest_url(key),
                                                                 data,
                                                                 get_header(data[2:40]),
                                                                 get_cookies(acc_token),
                                                                 acc_proxy)
                            if resp == 200:
                                logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                            elif resp == 400:
                                logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                            else:
                                logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING '
                                             f'WENT WRONG')
                            time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_join():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["join"].items():
                        if not key in {"08ebac1b-18e4-4807-80c2-b70fa1882cd9"}:
                            resp, warn = await send_post_request(session,
                                                                 get_quest_url(key),
                                                                 data,
                                                                 get_header(data[2:40]),
                                                                 get_cookies(acc_token),
                                                                 acc_proxy)
                            if resp == 200:
                                logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                            elif resp == 400:
                                logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                            else:
                                logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING '
                                             f'WENT WRONG')
                            time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_twitter():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["twitter"].items():
                        if data != "":
                            resp, warn = await send_post_request(session,
                                                                 get_quest_url(key),
                                                                 data,
                                                                 get_header(data[2:40]),
                                                                 get_cookies(acc_token),
                                                                 acc_proxy)
                            if resp == 200:
                                logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                            elif resp == 400:
                                logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                            else:
                                logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING '
                                             f'WENT WRONG')

                            time.sleep(2)
                        elif key == "6af63638-6c87-4caf-bade-a08ec1b42896":
                            boundary = '------WebKitFormBoundaryyrn9YrjQm5U5rTnW\r\nContent-Disposition: form-data; ' \
                                       'name="value"\r\n\r\n' + f'{tweet_links["spread"]}' + \
                                       '\r\n------WebKitFormBoundaryyrn9YrjQm5U5rTnW\r\nContent-Disposition: ' \
                                       'form-data; ' \
                                       'name="questId"\r\n\r\n6af63638-6c87-4caf-bade-a08ec1b42896\r\n' \
                                       '------WebKitFormBoundaryyrn9YrjQm5U5rTnW\r\nContent-Disposition: form-data; ' \
                                       'name="type"\r\n\r\ntwitter\r\n------WebKitFormBoundaryyrn9YrjQm5U5rTnW--\r\n '
                            resp, warn = await send_post_request(session,
                                                                 get_quest_url(key),
                                                                 data,
                                                                 get_header(boundary[2:40]),
                                                                 get_cookies(acc_token),
                                                                 acc_proxy)
                            if resp == 200:
                                logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                            elif resp == 400:
                                logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                            else:
                                logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT WRONG')
                            time.sleep(2)

                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_partner_twitter():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:

                    for key, data in quests["partner_twitter"].items():
                        resp, warn = await send_post_request(session,
                                                             get_quest_url(key),
                                                             data,
                                                             get_header(data[2:40]),
                                                             get_cookies(acc_token),
                                                             acc_proxy)
                        if resp == 200:
                            logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                        elif resp == 400:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')

                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_suiswap_friend():
        for acc_token, acc_proxy in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["suiswap_friend"].items():
                        resp, warn = await send_post_request(session,
                                                             get_quest_url(key),
                                                             data,
                                                             get_header(data[2:40]),
                                                             get_cookies(acc_token),
                                                             acc_proxy)
                        if resp == 200:
                            logger.info(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SUCCESS')
                        elif resp == 400:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')
                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")

    @staticmethod
    async def claim_all():
        pass

    @staticmethod
    async def get_xp(access_token):
        async with aiohttp.ClientSession() as session:
            result = await send_get_request(session, profile_link, GET_header, get_cookies(access_token))
            print(f'{result["discordHandle"]:20}Xp: {result["xp"]:2}   Level: {result["level"]}')


def main():
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(ZealyClient.get_xp(
    #     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJkNGIxMTZjMS0zZmMxLTRmYTMtYmQ4NS04MzI4OTk5YzM4YzUiLCJhY2NvdW50VHlwZSI6ImRpc2NvcmQiLCJpYXQiOjE2ODEyMzIxMjUsImV4cCI6MTY4MzgyNDEyNX0.vv-7l-uFBM0UrT1fjut7Q8dkSmqgW3EgnvGX0HgonP0'))
    loop.run_until_complete(ZealyClient.claim_partner_twitter())


if __name__ == "__main__":
    main()
