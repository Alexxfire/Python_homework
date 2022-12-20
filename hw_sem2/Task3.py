# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def Proverka(n):                 #определяем функцию проверки
    if n < 1:
        print('Число не положительное')
        exit()

def Main(array):                  #определяем основную функцию 
    i = 1
    while i < n+1:
        array[i-1] = round((1 + 1/i)**i,2)    #заполняем массив по формуле
        i = i+1
    print(array)
    i = 0
    while i < n:                    
        array[i] = round((array[i-1] + array[i]),0)     #находим суммы с округлением
        array[i] = int(array[i])                        #переводим в целое число
        i = i+1
    return(array)

try:                                #проверка на ввод букв
    n = int(input('Введите целое положительное число:'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(n)
result = [0]*n                 #задаем нулевой массив длиной N
print(f"N = {n} -> {Main(result)}")    