import requests


def get_lang_codes():
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    return response


def translate_text(text, target='ru', source='en'):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        'q': text,
        'target': target,
        'source': source,
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response


def get_horoscope(sign, day):
    signs = {
        'овен': 'Aries',
        'телец': 'Taurus',
        'близнецы': 'Gemini',
        'рак': 'Cancer',
        'лев': 'Leo',
        'дева': 'Virgo',
        'весы': 'Libra',
        'скорпион': 'Scorpio',
        'стрелец': 'Sagittarius',
        'козерог': 'Capricorn',
        'водолей': 'Aquarius',
        'рыбы': 'Pisces',
    }
    try:
        sign = signs[sign]  # сохраняем знак из словаря
        url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
        querystring = {"sign": sign, "day": day}
        headers = {
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        return response.json()
    except KeyError:
        print('Invalid sign')


sign = input('Знак зодиака: ')
day = 'tomorrow'
horo = get_horoscope(sign, day)
print(f'Horo: {horo["description"]}')
print(f'Compatibility: {horo["compatibility"]}')
