# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
chetvert = int(input('Введите четверть:'))
if chetvert < 1 or chetvert > 4:
    print('введите цифру от 1 до 4')
else:
    if chetvert ==1: 
        print ('Диапазон x =',x,'; y =',y,' -> 1')
    if x > 0 and y < 0: 
        print ('x =',x,'; y =',y,' -> 4')
    if x < 0 and y > 0: 
        print ('x =',x,'; y =',y,' -> 2')
    if x < 0 and y < 0: 
        print ('x =',x,'; y =',y,' -> 3')
