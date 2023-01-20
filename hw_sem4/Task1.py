# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def Proverka(n):                 #проверка на положительное число
    if n < 0:
        print('Число не положительное')
        exit()

try:                                #проверка на ввод букв
    N = int(input('Введите целое положительное число - точность числа PI:'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(N)
from math import pi
print("Через округление:",round(pi,N)) 
print("Через форматирование: {:.{}f}".format(pi, N))