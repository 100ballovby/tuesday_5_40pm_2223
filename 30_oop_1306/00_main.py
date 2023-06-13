class Person:  # класс - это шаблон (инструкция), по которой конструируется сущность в коде
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_name(self):  # метод (функция, которая принадлежит ТОЛЬКО классу), который пишет имя человека
        print(f'{self.name} says: Hello, my name is {self.name}!')

    def say_age(self):
        print(f'{self.name} says: Hello, my age is {self.age}!')

    def say_gender(self):
        print(f'{self.name} says: Hello, my gender is {self.gender}')


oleg = Person('Oleg', 20, 'Male')  # экземпляр класса Person
oksana = Person('Oksana', 25, 'Male')  # экземпляр класса Person
margarita = Person('Margarita', 55, 'Female')  # экземпляр класса Person

oleg.say_name()
margarita.say_age()
oksana.say_gender()
oksana.gender = 'Female'
oksana.say_gender()
oleg.say_gender()


