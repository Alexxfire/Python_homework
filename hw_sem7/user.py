import export

def Privet():
    k = int(input('****БД <Телефонный справочник> приветствует Вас!****\n> Укажите Ваше действие:\n'\
                    '1 - Поиск в справочнике \n' \
                    '2 - Добавление данных в справочник\n'\
                    '3 - Экспорт всего справочника\n'\
                    '4 - Выход из программы\n'))
    return k

def Posle_poiska():
    n = int(input('Что делаем дальше?:\n'\
                    '1 - Новый поиск \n' \
                    '2 - Экспортировать результаты поиска \n'\
                    '3 - Редактировать результаты поиска \n'))
    return n

def Vybor(result):
    import find
    step = Posle_poiska()
    if step == 1:
        find.Poisk()
    elif step == 2:
        export.Tel(result)
    elif step == 3:
        print('write') 
        #exit()

def New_kont():
    kon = True
    while kon == True:
        kontakt = ['']
        fam = input('Введите Фамилию нового контакта  -> ')
        im = input('Введите Имя нового контакта  -> ')
        ot = input('Введите Отчество нового контакта  -> ')
        tel = input('Введите телефон нового контакта в формате "+7......." без дефисов  -> ')
        kontakt[0] = fam+' '+im+' '+ot+' '+tel
        print(*kontakt)
        n = int(input('Контакт верен, записываем в БД?:\n'\
                        '1 - ДА \n' \
                        '2 - НЕТ, надо поправить \n'\
                        '3 - Передумал\n'))
        if n == 3:
            exit()
        elif n == 1:
            kon = False
    return kontakt