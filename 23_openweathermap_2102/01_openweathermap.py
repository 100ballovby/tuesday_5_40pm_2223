import requests as r
import json
import os


def get_data(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city,
              'appid': os.environ.get('API_KEY'),
              'units': 'metric',
              'lang': 'ru'}
    # получаем ключ API из переменной среды
    resp = r.get(url, params=params)
    return resp.json()

cities = ["Moscow", "Minsk", "Paris", "Riga", "Warsaw", "Vilnius"]

for city in cities:
    weather = get_data(city)
    print(f'Город {weather["name"]}')
    print(f'Сейчас {weather["weather"][0]["description"]}')
    print(f'Температура: {weather["main"]["temp"]} C')
    print(f'Ощущается как: {weather["main"]["feels_like"]} C')
    print()  # пустая строка между выводов



