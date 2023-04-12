import asyncio

from art import text2art
from ZealyClient import ZealyClient
from config.tokens import token_to_proxies


menu_options = {
    '1': 'Claim',
    '2': 'Show account xp',
    'q': 'quit',
}

sub_menu_options = {
    '1': 'Claim all quests',
    '2': 'Claim Onboarding',
    '3': 'Claim Special',
    '4': 'Claim Special Gift',
    '5': 'Claim Join',
    '6': 'Claim Invites',
    '7': 'Claim Boost',
    '8': 'Claim Quiz',
    '9': 'Claim Twitter',
    '10': 'Claim Partner Twitter Follow',
    '11': 'Claim Suiswap Friend Follow',
    '12': 'Claim Twitter',
    'q': 'quit',
}

menu_name_to_class_method = {
    'Claim all quests': "claim_all",
    'Claim Onboarding': "claim_onboarding",
    'Claim Special': "claim_special",
    'Claim Special Gift': "claim_special_gift", # disabled
    'Claim Join': "claim_join",
    'Claim Invites': "claim_invites", # disabled
    'Claim Boost': "claim_boost",
    'Claim Quiz': "claim_quiz",
    'Claim Twitter': "claim_twitter",
    'Claim Partner Twitter Follow': "claim_partner_twitter",
    'Claim Suiswap Friend Follow': "claim_suiswap_friend",
    'Show accounts xp': ''
}


def main():
    client = ZealyClient()
    while True:
        # Print the menu options
        print('Choose what u want to do:')
        for key, value in menu_options.items():
            print(f"{key}. {value}")

        # Prompt the user for their choice
        choice = input('> ')

        # Call the appropriate function or quit
        if choice in menu_options:
            if choice == '1':
                # Print the menu options
                print('Choose what u want to do:')
                for key, value in sub_menu_options.items():
                    print(f"{key}. {value}")

                # Prompt the user for their choice
                sub_choice = input('> ')
                if sub_choice in sub_menu_options:
                    function_name = sub_menu_options[sub_choice]

                    if function_name == 'quit':
                        continue
                    else:
                        function = getattr(client, menu_name_to_class_method[function_name])
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(function())

                else:
                    print('Invalid choice')

            else:
                function_name = menu_options[choice]

                if function_name == 'quit':
                    break
                else:
                    for token, _ in token_to_proxies.items():
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(ZealyClient.get_xp(token))
                    print('\n')
        else:
            print('Invalid choice')

if __name__ == "__main__":
    print(text2art('Suiswap Claimer'))
    main()
