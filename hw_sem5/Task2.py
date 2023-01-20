# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

def Vvod():         #ввод кол-ва конфет, проверка на ввод букв и число больше 100
    while True:
        try:                                
            confet = int(input('Введите целое положительное число больше 100 - количество конфет:'))
        except ValueError:
            print('введено не число / не целое число')
            continue
        if confet < 100 :
            print('Число меньше 100')
        else:
            break
    print(f'На столе лежит {confet} конфет')
    return confet


def Vvod1(x):         #сколько забираем конфет, проверка на ввод букв и число от 0 до 28
    while True:
        try:                                
            confet = int(input(f'Игрок {x} сколько конфет вы забираете? Не более 28шт. -> '))
        except ValueError:
            print('введено не число / не целое число')
            continue
        if confet < 1 or confet > 28:
            print('Число должно быть больше 0 и меньше 29')
        else:
            break
    return confet


def Next(hod):        #переход хода, 1 или 2 игрок
    if hod == 1:
        hod += 1
    else:
        hod -= 1
    return hod


def Game(conf, hod):         #игра
    while conf > 28:
        i = Vvod1(hod)        #игрок сколько конфет забираешь?
        conf = conf - i       #осталось конфет на столе
        if conf <= 28:
            print(f'Осталось 28 конфет или меньше, их забирает игрок {Next(hod)} и выигрывает!')
            exit()
        else:
            print(f'Осталось {conf} конфет')
            hod = Next(hod)     #переход хода


def main():
    conf = Vvod()
    input("Нажмите ENTER, чтобы разыграть первый ход")
    from random import randint
    hod = randint(1,2)                    #кто первый ходит - рандомный выбор
    print(f'Первым ходит игрок {hod}')
    Game(conf,hod)


if __name__ == "__main__":
	main()