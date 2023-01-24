import user

def Add():
    ff = open('file.txt', 'a')
    kontakt = user.New_kont()
    kontakt1 = str(kontakt[0])
    kontakt1 = kontakt1.encode('UTF-8').decode('UTF-8')    
    ff.write('\n')
    ff.write(kontakt1)    
    ff.close()
    print('Контакт успешно добавлен в БД!')