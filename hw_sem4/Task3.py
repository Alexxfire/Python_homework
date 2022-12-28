# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def Main(array):
    array2 = []
    for i in array:
        if i not in array2:
            array2.append(i)
    return(array2)

array = input("Введите числа через пробел: ").split()
try:                               #проверка на ввод букв
    array = list(map(int, array))
except ValueError:
    print('введено не число / не целое число')
    exit()

print(array)
print(f"Неповторяющиеся элементы -> {Main(array)}")


# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")