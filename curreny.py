

import requests
import time

url = 'https://cash.rbc.ru/cash/json/converter_currency_rate/?currency_from=RUR&currency_to=USD&source=cbrf&sum=100&date='

def convert(val1: str, val2: str, sm: int):
    url = 'https://cash.rbc.ru/cash/json/converter_currency_rate/?'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'currency_from': val1,
        'currency_to': val2,
        'source': 'cbrf',
        'sum': sm
    }

    response = requests.get(url=url, headers=headers, params=data)
    return response.json()['data']


print(convert('USD', 'RUR', 1))

while True:
    print(convert('USD', 'RUR', 1))
    time.sleep(15)
