import asyncio

from art import text2art
from ZealyClient import ZealyClient
from config.params import parse_tokens

menu_options = {
    '1': 'Claim',
    '2': 'Show account xp',
    '3': 'Get all xp',
    'q': 'quit',
}

sub_menu_options = {
    '1': 'Claim all quests',
    '2': 'Claim Onboarding',
    '3': 'Claim Special',
    '4': 'Claim Special Gift - disabled',
    '5': 'Claim Join',
    '6': 'Claim Invites - disabled',
    '7': 'Claim Boost',
    '8': 'Claim Quiz',
    '9': 'Claim Twitter',
    '10': 'Claim Partner Twitter Follow',
    '11': 'Claim Suiswap Friend Follow',
    '12': 'Claim new twitter quests',
    '13': 'Claim new quiz',
    'q': 'quit',
}

menu_name_to_class_method = {
    'Claim all quests': "claim_all",
    'Claim Onboarding': "claim_onboarding",
    'Claim Special': "claim_special",
    'Claim Special Gift - disabled': "claim_special_gift", # disabled
    'Claim Join': "claim_join",
    'Claim Invites - disabled': "claim_invites", # disabled
    'Claim Boost': "claim_boost",
    'Claim Quiz': "claim_quiz",
    'Claim Twitter': "claim_twitter",
    'Claim Partner Twitter Follow': "claim_partner_twitter",
    'Claim Suiswap Friend Follow': "claim_suiswap_friend",
    'Claim new twitter quests': "claim_new_twitter",
    'Claim new quiz': "claim_new_quiz"
}


def main():
    client = ZealyClient()
    while True:
        print('Choose what u want to do:')
        for key, value in menu_options.items():
            print(f"{key}. {value}")

        choice = input('> ')

        if choice in menu_options:
            if choice == '1':
                print('Choose what u want to do:')
                for key, value in sub_menu_options.items():
                    print(f"{key}. {value}")

                sub_choice = input('> ')
                if sub_choice in sub_menu_options:
                    function_name = sub_menu_options[sub_choice]

                    if function_name == 'quit':
                        continue
                    elif function_name == 'Claim Special Gift - disabled' or function_name == 'Claim Invites - disabled':
                        print("This function is currently not available.\n")
                        continue
                    else:
                        function = getattr(client, menu_name_to_class_method[function_name])
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(function())

                else:
                    print('Invalid choice')

            elif choice == '2':
                function_name = menu_options[choice]

                if function_name == 'quit':
                    break
                else:
                    token_to_proxies = parse_tokens("./config/tokens.txt")
                    for token in token_to_proxies.keys():
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(ZealyClient.get_xp(token))
                    print('\n')

            else:
                function_name = menu_options[choice]

                if function_name == 'quit':
                    break
                else:
                    token_to_proxies = parse_tokens("./config/tokens.txt")
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(ZealyClient.get_all_xp(token_to_proxies))
                    print('\n')

        else:
            print('Invalid choice')

if __name__ == "__main__":
    print(text2art('Suiswap Claimer'))
    main()
