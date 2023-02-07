import json
import requests


def make_request(url):
    req = requests.get(url)
    return req.json()  # возвращаю ответ сервера в формате JSON

link = "https://jsonplaceholder.typicode.com/todos"
result = make_request(link)

link_2 = "https://jsonplaceholder.typicode.com/users"
result_2 = make_request(link_2)

sum = 0
for task in result:
    if not task["completed"]:  # если статус completed == false
        print(task["id"])  # вывести значение ключа id
        sum += 1  # увеличить сумму

print(f'Не выполнено задач: {sum}')

users_tasks = {}
for task in result:
    if task["completed"]:
        if task["userId"] not in users_tasks:  # если id пользователя не в словаре с юзерами
            users_tasks[task["userId"]] = 1  # добавляем его id как новый ключ и пишем, что он не выпоолнил 1 задачу
        else:  # если id пользователя ЕСТЬ в словаре с юзерами
            users_tasks[task["userId"]] += 1  # добавляем к количеству выполненых задач 1

users = {}
for user in result_2:
    users[user["id"]] = user["name"]


for key in users.keys():
    print(f'{users[key]} completed {users_tasks[key]} tasks')

