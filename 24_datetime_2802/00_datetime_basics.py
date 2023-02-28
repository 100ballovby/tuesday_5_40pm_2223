import datetime as dt

now = dt.datetime.now()
print(now)

birthday = dt.datetime(year=2001, month=5, day=13, hour=16, minute=23)
print(birthday.date())
print(birthday.time())

# дельта - временная разница между двумя событиями
delta = now - birthday
print(delta)

# узнаем дату из прошлого
ancient = now - dt.timedelta(days=4)
theDayBefore = dt.date.today() - dt.timedelta(days=56)
print(ancient)
print(theDayBefore)

# разобрать время на элементы
print(f'Today year: {now.year}')
print(f'Today hour: {now.hour}')
print(f'Today min: {now.minute}')

# Получаем день недели
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f'Today is {days[now.weekday()]}')
"""
weekday() возвращает номер дня недели, 
обратите внимание, что понедельник - это 0 
"""

