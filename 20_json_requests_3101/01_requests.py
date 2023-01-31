"""
GET - запросы для получения информации от ресурса/БД/сервера
POST - запросы для передачи информации к ресурсу/БД/серверу
"""
import requests

request = requests.get("https://google.com/")
print(request)
print(request.text)

"""
1xx - подключение совершено, но сервер "думает"
2xx - успешное подключение к ресурсу 
3xx - (301, 303) - коды перенаправления (с vkontakte.ru на vk.com)

Коды ошибок 
4xx - (404) - страница не найдена (код ошибки пользователя), 403 - доступ запрещен 
5xx - (502) - ошибка ответа сервера (bad gateway) - код ошибки программиста  
"""


