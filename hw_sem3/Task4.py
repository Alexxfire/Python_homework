# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def Proverka(n):                 #определяем функцию проверки на положительное число
    if n < 0:
        print('Число не положительное')
        exit()

try:                                #проверка на ввод букв
    number = int(input('Введите положительное десятичное число:'))
except ValueError:
    print('введено не число / не целое число')
    exit()
Proverka(number)
a = str(bin(number))
print(f"{number} ->  {a[2:]}")      #удаляем первые 2 знака 0b