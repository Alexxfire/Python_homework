# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x, y = int(input('Введите координату X точки:')), int(input('Введите координату Y точки:'))
if x == 0 and y == 0:
    print('введите другие координаты, отличные от 0')
else:
    if x > 0 and y > 0: 
        print ('x =',x,'; y =',y,' -> 1')
    if x > 0 and y < 0: 
        print ('x =',x,'; y =',y,' -> 4')
    if x < 0 and y > 0: 
        print ('x =',x,'; y =',y,' -> 2')
    if x < 0 and y < 0: 
        print ('x =',x,'; y =',y,' -> 3')