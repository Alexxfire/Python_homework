# Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from functools import reduce
number = int(input('Введите целое число:'))
list_1 = [x for x in range(1,number+1)]
print(list_1)
list_2 = [1]*(number)
for i in range(1,number):
    list_2[i] = reduce(lambda x,y: x*y, list_1[:i+1])  
print(list_2)