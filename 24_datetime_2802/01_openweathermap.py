import requests as r
import datetime as dt
import os


def get_data(city):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "units": "metric",
        "lang": "ru",
        "q": city,
        "appid": os.environ.get("API_KEY"),
    }
    res = r.get(url, params=params)
    return res.json()


res = get_data("Minsk")
for cast in res["list"]:
    date = dt.datetime.fromtimestamp(cast["dt"])  # трансформируем timestamp в дату (нормальную)
    if date.hour == 18:  # если часы равны 18
        local_date = date.strftime("%A, %d %B %Y | %H:%M")
        temp = cast["main"]["temp"]
        feels = cast["main"]["feels_like"]
        descr = cast["weather"][0]["description"]
        print(f"Date: {local_date}\nTemp: {temp}\nFeels: {feels}\nDescription: {descr}\n\n")


"""
%a: возвращает первые три символа дня недели, например. Tue
%A: возвращает полное название дня недели, например. Tuesday.
%B: возвращает полное название месяца, например. September.
%w: возвращает день недели в виде числа от 0 до 6, где воскресенье равно 0.
%m: возвращает месяц в виде числа от 01 до 12.
%p: возвращает AM/PM для времени.
%y: возвращает год в двузначном формате, то есть без века. Например, «18» вместо «2018».
%f: возвращает микросекунды от 000000 до 999999.
%Z: возвращает часовой пояс.
%z: возвращает смещение UTC.
%j: возвращает номер дня в году от 001 до 366.
%W: возвращает номер недели в году от 00 до 53, при этом понедельник считается первым днем недели.
%U: возвращает номер недели в году от 00 до 53, при этом воскресенье считается первым днем каждой недели.
%c: возвращает локальную версию даты и времени.
%x: возвращает локальную версию даты.
%X: возвращает локальную версию времени.
"""

