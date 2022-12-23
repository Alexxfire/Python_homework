# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def Proverka(n):                 #определяем функцию проверки на положительное число
    if n < 1:
        print('Число не положительное')
        exit()

def RandomArray(N):               #определяем функцию генерации массива
    from random import randint
    array = [0]*N
    for i in range(N):
        array[i] = randint(1,9)
    return(array)

def Main(array):                  #определяем функцию поиска нечетных позиций и этих элементов
    array2 = []
    for i in range(len(array)):
        if i%2 != 0:
            array2.append(array[i])    #копируем нужные элементы в конец нового массива
    return(array2)    

try:                                #проверка на ввод букв
    N = int(input('Введите целое положительное число - размер массива:'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(N)
array_main = []
array_main = RandomArray(N)
print(array_main)
array_nechet = Main(array_main)
print(f"на нечетных позицях {array_nechet} их сумма: {sum(array_nechet)}") 