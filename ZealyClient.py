import asyncio
import time
import aiohttp

from config.quests import quests
from config.params import get_cookies, get_header, get_quest_url,  profile_link, GET_header, parse_tokens
from config.logger import logger
from config.tweet_links import tweet_links
from routes import send_post_request, send_get_request, get_me


class ZealyClient:
    def __init__(self):
        self.base_url = "https://api.zealy.io/communities/suiswap-app/quests"
        self.token_to_proxies = parse_tokens("./config/tokens.txt")

    async def claim_onboarding(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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
                        elif resp == 422:
                            logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                        else:
                            logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING WENT '
                                         f'WRONG')
                        time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")


    async def claim_special(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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


    async def claim_quiz(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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


    async def claim_boost(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:
                    for key, data in quests["boost"].items():
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


    async def claim_join(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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
                            elif resp == 402:
                                logger.warning(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- {warn}')
                            else:
                                logger.error(f'#{key[0:4]} RESPONSE by {user_name}: STATUS CODE {resp} --- SOMETHING '
                                             f'WENT WRONG')
                            time.sleep(2)
                except aiohttp.ClientError as err_:
                    logger.error(f"ERROR: {err_}")


    async def claim_twitter(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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


    async def claim_partner_twitter(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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


    async def claim_suiswap_friend(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
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


    async def claim_all(self):
        methods = [self.claim_suiswap_friend, self.claim_partner_twitter, self.claim_twitter,
                   self.claim_join, self.claim_boost, self.claim_onboarding, self.claim_special,
                   self.claim_quiz]
        for method in methods:
            await method()


    @staticmethod
    async def get_xp(access_token):
        async with aiohttp.ClientSession() as session:
            result = await send_get_request(session, profile_link, GET_header, get_cookies(access_token))
            print(f'{result["discordHandle"]:20}Xp: {result["xp"]:2}   Level: {result["level"]}')


    @staticmethod
    async def get_all_xp(token_to_proxies):
        xp = 0
        for access_token, _ in token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                result = await send_get_request(session, profile_link, GET_header, get_cookies(access_token))
                xp += result["xp"]
        print(f"XP: {xp}")


    async def claim_new_twitter(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:

                    for key, data in quests["new_twitter"].items():
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

    async def claim_new_quiz(self):
        for acc_token, acc_proxy in self.token_to_proxies.items():
            async with aiohttp.ClientSession() as session:
                user_name = await get_me(acc_token)
                try:

                    for key, data in quests["new_quiz"].items():
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