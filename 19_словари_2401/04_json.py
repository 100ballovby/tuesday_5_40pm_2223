import json

data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },  # индекс 0
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },  # индекс 1
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        },  # индекс 2
    ]
}

"""
dump() - превращает словарь/список python в поток JSON для записи в файл 
dumps() - превращает словарь/список python в строку JSON 
"""
def dict_to_json(obj, filename):
    json_str = json.dumps(obj, indent=4)  # конвертировать в JSON-строку словарь data
    # indent добавляет отступы в JSON-строку
    with open(filename, "w") as json_file:
        json_file.write(json_str)


def json_to_dict(file):
    with open(file, "r"):



