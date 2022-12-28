# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def Proverka(n):                 #проверка на натуральное число
    if n < 1:
        print('Число не натуральное')
        exit()

def Main(k):
    koeff=[randint(0,max_val) for i in range(k+1)]
    koeff = list(map(str,koeff))
    print(koeff)
    x = ['x**' + str(i) for i in range(k,-1,-1)]
    kx = [0]*(k+1)
    for j in range(0,k+1):
        kx[j] = koeff[j]+x[j]
    kx = "+".join(map(str, kx))
    kx=kx.replace('x**1+', 'x+')
    kx=kx.replace('x**0', '')
    kx = kx + ' = 0'
    print(kx)
    return(kx)

from random import randint
max_val=100
try:                                #проверка на ввод букв
    k = int(input('Введите натуральную степень k:'))
except ValueError:
    print('введено не число / не натуральное число')
    exit()
Proverka(k)
with open('file.txt', 'w') as data:
    data.write(Main(k))
data.close()