import json


def json_to_obj(json_file):
    with open(json_file, 'r') as file:
        data = json.loads(file.read())
    return data


def obj_to_json(obj, json_file):
    with open(json_file, 'w') as file:
        file.write(json.dumps(obj, indent=4))


todos = json_to_obj("todos.json")
users = json_to_obj("users.json")

tasks_per_user = {}
for task in todos:  # перебираем задачи
    if task["completed"]:  # если задача выполонена (completed: True)
        if task["userId"] not in tasks_per_user:  # если id нет в словаре
            tasks_per_user[task["userId"]] = {"completed": 1, "not_completed": 0}  # добавить этот id с новым словарем внутри
        else:  # если id есть в словаре
            tasks_per_user[task["userId"]]["completed"] += 1  # увеличить количество выполненных на 1
    if not task["completed"]:  # если задача не выполонена (completed: False)
        if task["userId"] not in tasks_per_user:  # если id нет в словаре
            tasks_per_user[task["userId"]] = {"completed": 0, "not_completed": 1}  # добавить этот id с новым словарем внутри
        else:  # если id есть в словаре
            tasks_per_user[task["userId"]]["not_completed"] += 1  # увеличить количество невыполненных на 1

print(tasks_per_user)

usernames = {}
for u in users:
    usernames[u["id"]] = u["name"]

print(usernames)
for key in tasks_per_user.keys():
    completed = tasks_per_user[key]['completed']
    not_completed = tasks_per_user[key]['not_completed']
    total_tasks = completed + not_completed  # общее количество задач каждого юзера
    kpi = (completed / total_tasks) * 100
    print(f"User: {usernames[key]}:")
    print(f"Completed: {completed} tasks;")
    print(f"Didn't completed: {not_completed} tasks.")
    print(f"KPI: {kpi}%.")
    print()



