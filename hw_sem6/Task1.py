# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11
from functools import reduce
number = input('Введите вещественное число:')
print(number)
new = list(filter(lambda x: (x.isdigit() == True), number))   #оставляем только цифры
print(new)
print(reduce(lambda x, y: int(x) + int(y), new))              #выводим сумму