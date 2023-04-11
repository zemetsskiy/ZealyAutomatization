import aiohttp
import requests

from config.tokens import access_token

cookies = {
            'subdomain': 'suiswap-app',
            'access_token': access_token,
            'cookie-config': '{%22functional%22:true%2C%22analytics%22:true%2C%22marketing%22:true}',
            }

#TODO для каждого квиза необходимо собирать 3 переменные: boundary, data, url


# использовались для тестирования. ПОРЯДОК НАРУШЕН
boundary_1 = '----WebKitFormBoundaryjUHMRYpNR0GvSyrx'
boundary_2 = '----WebKitFormBoundaryCpaT065qDqJJcFtD'
boundary_3 = '----WebKitFormBoundaryZJwTdQmZ5nuJMABH'


headers = {
    'authority': 'api.zealy.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data;' + f' boundary={boundary_3}',
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

class ZealyClient:
    # claim link ex: https://api.zealy.io/communities/suiswap-app/quests/b7c3412f-c534-45dc-baf7-fbaee7fdd085/claim
    def __init__(self):
        self.base_url = "https://api.zealy.io/communities/suiswap-app/quests"

    def claim_onboarding(self):
        pass

    def claim_special(self):
        pass

    @staticmethod
    def claim_quiz():

        # TODO: добавить эти юрлы даты и бондари в конфиг
        # TODO: не забываеем сверху оставлять комментарий что за тема вопроса, чтобы не запутаться


        #What is Suiswap
        data_1 = '------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="value"\r\n\r\nA unified swapping platform built on SUI\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="questId"\r\n\r\n192a1798-70a9-4939-9da2-73ed0374451d\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg--\r\n'
        url_1 = 'https://api.zealy.io/communities/suiswap-app/quests/192a1798-70a9-4939-9da2-73ed0374451d/claim'

        # data on  Suiswap Project Start
        data_2 = '------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="value"\r\n\r\n2022.9\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="questId"\r\n\r\nfb55fe60-0ae5-485c-bdec-1f66004248de\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ--\r\n'
        url_2 = 'https://api.zealy.io/communities/suiswap-app/quests/fb55fe60-0ae5-485c-bdec-1f66004248de/claim'

        data_3 = '------WebKitFormBoundaryQDxD5TQRvA7DgjdW\r\nContent-Disposition: form-data; name="value"\r\n\r\nA community point that can be redeemed for airdrop\r\n------WebKitFormBoundaryQDxD5TQRvA7DgjdW\r\nContent-Disposition: form-data; name="questId"\r\n\r\ned4254cc-9ecd-41c5-aa49-46be5ecbfa0d\r\n------WebKitFormBoundaryQDxD5TQRvA7DgjdW\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundaryQDxD5TQRvA7DgjdW--\r\n'
        url_3 = 'https://api.zealy.io/communities/suiswap-app/quests/ed4254cc-9ecd-41c5-aa49-46be5ecbfa0d/claim'

        data_4 = '------WebKitFormBoundarygEbgZnwKtglNUJvM\r\nContent-Disposition: form-data; name="value"\r\n\r\nExchange for Suiswap token after mainnet launch\r\n------WebKitFormBoundarygEbgZnwKtglNUJvM\r\nContent-Disposition: form-data; name="questId"\r\n\r\n622fc736-a524-4692-9620-bf00aae9eaab\r\n------WebKitFormBoundarygEbgZnwKtglNUJvM\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundarygEbgZnwKtglNUJvM--\r\n'
        url_4 = 'https://api.zealy.io/communities/suiswap-app/quests/622fc736-a524-4692-9620-bf00aae9eaab/claim'

        data_5 = '------WebKitFormBoundary5yLGwz7NIQBcocr0\r\nContent-Disposition: form-data; name="value"\r\n\r\nYES\r\n------WebKitFormBoundary5yLGwz7NIQBcocr0\r\nContent-Disposition: form-data; name="questId"\r\n\r\na801e865-dc48-478b-a784-2e963510f7e3\r\n------WebKitFormBoundary5yLGwz7NIQBcocr0\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundary5yLGwz7NIQBcocr0--\r\n'

        url_6 = 'https://api.zealy.io/communities/suiswap-app/quests/0d3fccc4-f4f4-4785-aa60-0826382f774d/claim'
        data_6 = '------WebKitFormBoundarypBQh9RnBigKSaOno\r\nContent-Disposition: form-data; name="value"\r\n\r\nYES\r\n------WebKitFormBoundarypBQh9RnBigKSaOno\r\nContent-Disposition: form-data; name="questId"\r\n\r\n0d3fccc4-f4f4-4785-aa60-0826382f774d\r\n------WebKitFormBoundarypBQh9RnBigKSaOno\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundarypBQh9RnBigKSaOno--\r\n'

        url_7 = 'https://api.zealy.io/communities/suiswap-app/quests/6a120dfe-4e01-4fda-a1c6-d1dc9d740546/claim'
        data_7 = '------WebKitFormBoundaryjUHMRYpNR0GvSyrx\r\nContent-Disposition: form-data; name="value"\r\n\r\nYES\r\n------WebKitFormBoundaryjUHMRYpNR0GvSyrx\r\nContent-Disposition: form-data; name="questId"\r\n\r\n6a120dfe-4e01-4fda-a1c6-d1dc9d740546\r\n------WebKitFormBoundaryjUHMRYpNR0GvSyrx\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundaryjUHMRYpNR0GvSyrx--\r\n'

        url_8 = 'https://api.zealy.io/communities/suiswap-app/quests/ee561f58-8be3-4853-9faf-46212c2a8a4a/claim'
        data_8 = '------WebKitFormBoundaryCpaT065qDqJJcFtD\r\nContent-Disposition: form-data; name="value"\r\n\r\nWeighted by the Suiswap Points you have\r\n------WebKitFormBoundaryCpaT065qDqJJcFtD\r\nContent-Disposition: form-data; name="questId"\r\n\r\nee561f58-8be3-4853-9faf-46212c2a8a4a\r\n------WebKitFormBoundaryCpaT065qDqJJcFtD\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundaryCpaT065qDqJJcFtD--\r\n'

        url_9 = 'https://api.zealy.io/communities/suiswap-app/quests/6ae7a9b8-df63-49a6-bdad-470da36aa3c8/claim'
        data_9 = '------WebKitFormBoundaryZJwTdQmZ5nuJMABH\r\nContent-Disposition: form-data; name="value"\r\n\r\n$SSWP\r\n------WebKitFormBoundaryZJwTdQmZ5nuJMABH\r\nContent-Disposition: form-data; name="questId"\r\n\r\n6ae7a9b8-df63-49a6-bdad-470da36aa3c8\r\n------WebKitFormBoundaryZJwTdQmZ5nuJMABH\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundaryZJwTdQmZ5nuJMABH--\r\n'

        try:
            response = requests.post(
                url_9,
                cookies=cookies,
                headers=headers,
                data=data_9,
            )

            response.raise_for_status()  # raise exception for any HTTP error status codes
            print('Claim request successful!')
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}')
        except requests.exceptions.Timeout as err:
            print(f'Timeout error occurred: {err}')
        except requests.exceptions.ConnectionError as err:
            print(f'Connection error occurred: {err}')
        except requests.exceptions.RequestException as err:
            print(f'An error occurred: {err}')

    def claim_boost(self):
        pass

    def claim_join(self):
        pass

    def claim_twitter(self):
        pass

    def claim_partner_twitter(self):
        pass

    def claim_suiswap_friend(self):
        pass


def main():
    ZealyClient.claim_quiz()


if __name__ == "__main__":
        main()