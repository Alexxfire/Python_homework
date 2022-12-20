# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11
number = str(input('Введите вещественное число:'))
def DeletePoints(old):          #определяем функцию замены символов 
    new = ""
    for i in old:
        if i=="." or i=="," or i=="-":
            i="0"                          #символы меняем на 0
        new = new + i
    return(new)


def Sum(num):                  #определяем функцию суммирования 
    num = int(num)
    sum = 0
    while num >= 1:
        sum = sum + num%10      #добавляем последнюю цифру к сумме
        num = num//10           #сокращаем число на 1 разряд
    return(sum)


fin_sum = int()                 #переменная = результат
try:                            #проверка на буквы
    fin_sum = int(DeletePoints(number))
    print(f"{number} -> {Sum(fin_sum)}")
except ValueError:
    print('введено не число')