import os
import json
import requests
import subprocess
A = '\033[1;34m'#ازرق
X = '\033[1;33m' #اصفر

filename = 'matrix.json'

try:
    with open(filename, 'r') as f:
        data = json.load(f)
        api_id = data['api_id']
        api_hash = data['api_hash']
        bot_token = data['bot_token']
        id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token

        # Send a GET request to the Telegram API
        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
        response_data = response.json()

        # Extract bot_username from the response
        user_bot = response_data['result']['username']
except FileNotFoundError:
    api_id = 23398930
    print('  ')
    api_hash = 'bd3e85a7aae40566f2fa8804d200d6d0'
    print('  ')
    bot_token = input(A+"❖ Inter Your Token ➜  "+X)
    print('  ')
    id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token
    print('  ')

    # Send a GET request to the Telegram API
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
    response_data = response.json()

    # Extract bot_username from the response
    user_bot = response_data['result']['username']
    
    print('  ')
    
    data = {
        'api_id': api_id,
        'api_hash': api_hash,
        'bot_token': bot_token,
    }

    
    with open(filename, 'w') as f:
        json.dump(data, f)

responseee = requests.get("https://raw.githubusercontent.com/DevMatrixArabic125901/ma/main/MillionWinner.py")

with open('run.py', 'w') as file:
    file.write(responseee.text)

os.system('python3 MillionWinner.py')
