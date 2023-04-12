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

    def claim_boost(self):
        pass

    def claim_join(self):
        pass

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
    loop.run_until_complete(ZealyClient.claim_special())


if __name__ == "__main__":
     main()
