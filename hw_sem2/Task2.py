# Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def Proverka(n):                 #определяем функцию проверки
    if n < 1:
        print('Число не положительное')
        exit()

def Main(array):                  #определяем основную функцию 
    i = 0
    while i < number:
        jj = 1
        j = i+1
        while j > 0:
            jj = jj*j
            j = j-1
        array[i] = jj
        i = i+1
    return(array)

try:                                #проверка на ввод букв
    number = int(input('Введите целое положительное число:'))
except ValueError:
    print('введено не число / не целое число')
    exit()

Proverka(number)
result = [0]*number                 #задаем нулевой массив длиной N
print(f"N = {number} -> {Main(result)}")    