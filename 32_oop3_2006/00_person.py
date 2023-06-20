class Person:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f'Name {self.name}')
        print(f'Age: {self.age}')
        print(f'Salary: ${self.salary}')

    def setSalary(self, newSalary: float):
        if newSalary > 0:
            self.salary += newSalary
            print('Salary changed')
        else:
            print('Incorrect salary value')


m = Person('Max', 20, 5000)
m.display_info()
m.setSalary(400)
m.display_info()