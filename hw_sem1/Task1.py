# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
weekNumber = int(input('Введите число - день недели:'))
if weekNumber > 0 and weekNumber < 8:       #проверка
    if weekNumber > 5:
        print(weekNumber,' -> yes')
    else:
        print(weekNumber,' -> no')     
else:
    print('неверно введено число')