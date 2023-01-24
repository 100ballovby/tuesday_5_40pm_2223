data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ]
}

for i in range(len(data["employees"])):  # перебираю индексы из списка в employees
    person = data["employees"][i]  # перебираю по индексам все вложенные словари
    for key in person.keys():
        print(f"{key}: {person[key]}")
    print()
