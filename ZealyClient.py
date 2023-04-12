import asyncio
import aiohttp
import requests

from config.quests import quests
from config.params import cookies, get_header, get_quest_url


async def send_post_request(session, url, data, headers):
    async with session.post(url, data=data, headers=headers, cookies=cookies) as resp:
        result =  resp.status
        return result


class ZealyClient:
    # claim link ex: https://api.zealy.io/communities/suiswap-app/quests/b7c3412f-c534-45dc-baf7-fbaee7fdd085/claim
    def __init__(self):
        self.base_url = "https://api.zealy.io/communities/suiswap-app/quests"

    def claim_onboarding(self):
        pass

    @staticmethod
    async def claim_special():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["special"].items():
                result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                print(f'Response {key[0:4]}: {result}')

    @staticmethod
    async def claim_quiz():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["quiz"].items():
                result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                print(f'Response {key[0:4]}: {result}')

    @staticmethod
    async def claim_boost():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["boost"].items():
                if data != "":
                    result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                    print(f'Response {key[0:4]}: {result}')

    @staticmethod
    async def claim_join():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["join"].items():
                if not key in {"14237ce9-121f-4288-9c2a-e596987151cf", "08ebac1b-18e4-4807-80c2-b70fa1882cd9"}:
                    result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                    print(f'Response {key[0:4]}: {result}')

    def claim_twitter(self):
        pass

    @staticmethod
    async def claim_partner_twitter():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["partner_twitter"].items():
                result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                print(f'Response {key[0:4]}: {result}')

    @staticmethod
    async def claim_suiswap_friend():
        async with aiohttp.ClientSession() as session:
            for key, data in quests["suiswap_friend"].items():
                result = await send_post_request(session, get_quest_url(key), data, get_header(data[2:40]))
                print(f'Response {key[0:4]}: {result}')

    #TODO Получать XP каждого клиента


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ZealyClient.claim_join())


if __name__ == "__main__":
     main()
