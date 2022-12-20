#Реализуйте алгоритм перемешивания списка.
def Proverka(n):                 #определяем функцию проверки
    if n < 1:
        print('Число не положительное')
        exit()

def Mass(array,n):
    array2 = [0]*9
    k = 1
    while k <= n:                         #делаем итерации, кол-во которых вводим
        j = 0
        while j < 9:
            array2[j] = array[(j+5)%9]    #сдвигаем массив вправо по кругу
            j = j+1
        i = 0
        temp = 0
        while i < 8:                      #меняем местами пары 
            temp = array2[i]
            array2[i] = array2[i+1]
            array2[i+1] = temp
            i= i+2
        array = array2[:]
        k=k+1
    return(array2)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:                                #проверка на ввод букв
    n = int(input('Введите целое положительное число - число итераций:'))
except ValueError:
    print('введено не число / не целое число')
    exit()
Proverka(n)
print(array)
print(Mass(array,n))