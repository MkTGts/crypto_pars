import requests
from bs4 import BeautifulSoup


def imported_names() -> list:  # достаем имена агентов
    url = 'https://bitality.cc/Home/Index/ZRX--BOND'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    names = [i['data-name'] for i in soup.find_all('div', class_='b-choose__item b-choose__valuteitem m-1')]

    with open('names_agent.txt', 'w', encoding='utf-8') as file:  
        file.write(';'.join(names))  # записываем в имена в файл

    return names  # возвращаем спиок имен

names = imported_names()  # список имен


def conversion(name1: str, name2: str, sm: int):  # конвертируем 
    url = 'https://bitality.cc/Home/GetSum?'  # шаблон url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'GiveName': name1,
        'GetName': name2,
        'sum': sm,
        'Direction': 0
    }

    response = requests.get(url=url, headers=headers, params=data)
    return {'in': name1, 'out': name2, 'count': sm, 'convert': response.json()['getSum']}




#imported_names()
d = conversion('0x', 'Aave', 100)
print(f'{d['count']} {d['in']}  =  {d['convert']} {d['out']}')
