from sys import argv

name, выработка, ставка, премия = argv

try:
    print(f'Зарплата сотрудника =', int(выработка) * int(ставка) + int(премия))
except ValueError:
    print("Введены не корректные данные")

