def All():
    gg = open('full.txt', 'a')
    ff = open('file.txt', encoding='UTF-8').readlines()
    for i in iter(ff):
        gg.write(i)
    print('Справочник экспортирован в файл full.txt')
    gg.close()

def Tel(data):
    ff = open('export.txt','w')     
    for i in data:
        ff.write(i)
    print('Данные успешно экспортированы в файл export.txt')
    ff.close()
