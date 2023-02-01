#игра креcтики-нолики
import emoji

def Board(i):    #вывод игрового поля
    print ('--------------------')
    print (f'  {i[0]}  |  {i[1]}   |  {i[2]}  |')
    print ('--------------------')
    print (f'  {i[3]}  |  {i[4]}   |  {i[5]}  |')
    print ('--------------------')
    print (f'  {i[6]}  |  {i[7]}   |  {i[8]}  |')
    print ('--------------------')


def Vvod(hod,field):         #выбор позиции для знака, запоминание, проверка на занятость
    while True:
        try:                                
            position = int(input(f'Игрок {hod} выберите номер поля для {XO(hod)} -> '))
        except ValueError:
            print('введено не число / не целое число')
            continue
        if (position < 1) or (position > 9):
            print('Число должно быть больше 0 и меньше 10')
            continue
        if (field[position-1] == emoji.emojize(":thumbsup:", language="alias")) or (field[position-1] == emoji.emojize(":red_heart:", variant="emoji_type")):
            print('поле уже занято, выберите другое')
            continue
        else:
            break
    field[position-1] = XO(hod)


def XO(hod):          #1игрок играет X 2игрок О
    if hod == 1:
        mark = emoji.emojize(":thumbsup:", language="alias")
    else:
        mark = emoji.emojize(":red_heart:", variant="emoji_type")
    return mark


def Next(hod):        #переход хода, 1 или 2 игрок
    if hod == 1:
        hod += 1
    else:
        hod -= 1
    return hod


def Proverka(field):    #проверка выигрыша
    result = ''
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    for i in win:
        if field[i[0]] == emoji.emojize(":thumbsup:", language="alias") and field[i[1]] == emoji.emojize(":thumbsup:", language="alias") and field[i[2]] == emoji.emojize(":thumbsup:", language="alias"):
            result = emoji.emojize(":thumbsup:", language="alias")
        if field[i[0]] == emoji.emojize(":red_heart:", variant="emoji_type") and field[i[1]] == emoji.emojize(":red_heart:", variant="emoji_type") and field[i[2]] == emoji.emojize(":red_heart:", variant="emoji_type"):
            result = emoji.emojize(":red_heart:", variant="emoji_type")   
    return result 


def Game(hod, field):
    finish = False
    count = 0
    while finish == False:
        if count == 9:
            Board(field)
            print('БОЕВАЯ НИЧЬЯ!!!')
            exit()
        else: 
            Board(field) 
            Vvod(hod, field)
            if Proverka(field) != '':
                finish = True
            else:
                finish = False
            hod = Next(hod)
            count +=1
    print(f'\n******Увы, игрок {XO(hod)}   проиграл :(')
    Board(field)
    input('Нажмите любую клавишу для завершения')


def main():
    input("Нажмите ENTER, чтобы разыграть первый ход")
    from random import randint
    hod = randint(1,2)                    #кто первый ходит - рандомный выбор
    print(f'Первым ходит игрок {hod}, ваш символ "  {XO(hod)}  "')
    field = [1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9  ]           #игровое поле
    Game(hod, field)


if __name__ == "__main__":
	main()