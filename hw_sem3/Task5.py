# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Proverka(n):                 #определяем функцию проверки 
    if n <= 0:
        print('Число не положительное')
        exit()

def Fibb (n): 
    k = 2
    fib = [0,1]
    antifib = []
    while k <= n:
        fib.append(fib[k-2]+fib[k-1])            #добавляем в конец массива числа фибоначчи
        antifib.insert(0,int((-1)**(k)*fib[k-1]))      #добавляем в начало массива числа негафибоначчи
        k +=1
    antifib.insert(0,int((-1)**(k)*fib[k-1]))     #добавляем последнее число негафибоначчи, не попавшее в цикл
    return(antifib+fib)

try:                                #проверка на ввод букв
    n = int(input('Введите положительное целое число больше "0":'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(n)
print(Fibb(n))