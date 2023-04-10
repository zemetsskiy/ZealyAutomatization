import aiohttp
import  requests

from config.tokens import access_token

cookies = {
            'subdomain': 'suiswap-app',
            'access_token': access_token,
            'cookie-config': '{%22functional%22:true%2C%22analytics%22:true%2C%22marketing%22:true}',
        }

headers = {
            'authority': 'api.zealy.io',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarya6kyALYmyxyvZbAQ',
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

        # TODO: добавить эти юрлы и даты в конфиг

        #What is Suiswap
        data_1 = '------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="value"\r\n\r\nA unified swapping platform built on SUI\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="questId"\r\n\r\n192a1798-70a9-4939-9da2-73ed0374451d\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundary9ir1X9Kxnl2G7srg--\r\n'
        url_1 = 'https://api.zealy.io/communities/suiswap-app/quests/192a1798-70a9-4939-9da2-73ed0374451d/claim'

        # data on  Suiswap Project Start
        data_2 = '------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="value"\r\n\r\n2022.9\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="questId"\r\n\r\nfb55fe60-0ae5-485c-bdec-1f66004248de\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ\r\nContent-Disposition: form-data; name="type"\r\n\r\nquiz\r\n------WebKitFormBoundarya6kyALYmyxyvZbAQ--\r\n'
        url_2 = 'https://api.zealy.io/communities/suiswap-app/quests/fb55fe60-0ae5-485c-bdec-1f66004248de/claim'

        try:
            response = requests.post(
                url_2,
                cookies=cookies, headers=headers, data=data_2)
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