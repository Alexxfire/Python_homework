#поиск информации в справочнике
def Poisk():
    import user
    kon = True
    while kon == True:
        mask = input('Введите ФИО или маску для поиска в справочнике \n')
        ff = open('file.txt', encoding='UTF-8').readlines()
        result = []
        for i in iter(ff):
            if mask in i.lower():
                print(i)
                result.append(i)
        if len(result) == 0:
            print('Поиск не дал результатов')
        else:
            kon = False
    user.Vybor(result)
    
#Poisk()