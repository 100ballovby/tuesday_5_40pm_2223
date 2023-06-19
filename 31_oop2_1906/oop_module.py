class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__grades = []  # инкапсулированные данные, то есть они спрятаны от внешней программы

    def get_grades(self):
        """
        метод-геттер, позволяет получить информацию,
        которая была инкапсулирована (сокрыта)
        :return: None
        """
        for i in range(len(self.__grades)):
            print(f"Grade {i}: {self.__grades[i]}")
        return self.__grades

    def set_grade(self, grade):
        self.__grades.append(grade)

    def get_average_grade(self):
        summ = 0
        for i in range(len(self.__grades)):
            summ += self.__grades[i]
        mark = summ / len(self.__grades)
        return mark


if __name__ == '__main__':
    s = Student('Igor', 15)
    s.set_grade(5)
    s.set_grade(3)
    s.set_grade(4)
    s_grades = s.get_grades()
    s_mid = s.get_average_grade()
    print(f'Middle mark: {s_mid}')

