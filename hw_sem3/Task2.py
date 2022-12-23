#  Напишите программу, которая найдёт произведение пар чисел списка. 
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def RandomArray(N):               #определяем функцию генерации массива
    from random import randint
    array = [0]*N
    for i in range(N):
        array[i] = randint(1,9)
    return(array)

def Main(array):                  #определяем функцию
    import math
    array2 = []
    i=0
    while i < math.ceil(len(array)/2):
        array2.append(array[i]*array[len(array)-1-i])    #копируем нужные элементы в конец нового массива
        i = i + 1
    return(array2)    

def Proverka(n):                 #определяем функцию проверки на положительное число
    if n < 1:
        print('Число не положительное')
        exit()

try:                                #проверка на ввод букв
    N = int(input('Введите целое положительное число - размер массива:'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(N)
array_main = []
array_main = RandomArray(N)
print(array_main, end="  ")
array_exit = Main(array_main)
print(f"произведение пар -> {array_exit}") 