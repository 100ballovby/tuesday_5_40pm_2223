from oop_module import *


jane = Student('Jane', 20)
bill = Student('Bill', 21)
jill = Student('Jill', 22)

jane.set_grade(5)
jane.set_grade(7)
jane.set_grade(9)

bill.set_grade(9)
bill.set_grade(6)

jill.set_grade(4)
jill.set_grade(6)
jill.set_grade(2)

print(f'{jill.name} middle mark: {jill.get_average_grade()}')
print(f'{jane.name} middle mark: {jane.get_average_grade()}')
print(f'{bill.name} middle mark: {bill.get_average_grade()}')

