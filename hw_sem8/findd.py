#поиск информации в журнале
import user
import csv
import main
import output
import write


def Poisk():
    Find_uchenik()


def Poisk_strok():             #поиск и вывод строки по ученику
    mask = input('Поиск можно осуществлять по номеру, фамилии, имени, классу или задать произвольную маску.\n')
    with open("school.csv", encoding='cp1251') as file1:
        file_reader = csv.reader(file1, delimiter = ";")
        result = []
        print(*next(file_reader))
        for row in file_reader:
            if mask.lower() in (''.join(row)).lower():
                print(*row)
                result.append(row)
    return result


def Find_uchenik():               #поиск ученика + выставление ему оценки
    step = True
    while step == True:
        result = Poisk_strok()
        if len(result) == 0:
            print('Поиск не дал результатов')
        else:
            step = False
    deystvie = user.Posle_poiska_uchenik()
    if deystvie == 1:
        Find_uchenik()
    elif deystvie == 2:
        output.Show_ocenki(result)
    elif deystvie == 3:
        if len(result) > 1:
            print('Оценку можно выставить одному ученику, выберите в поиске одного ученика, например, по уникальному номеру.')
            Find_uchenik()
        else:
            write.Ocenka(result)
    elif deystvie == 4:
        main.main()


def Poisk_id():                  #поиск максимального id, чтобы записать нового ученика
    with open("school.csv", encoding='cp1251') as file1:
        file_reader = csv.reader(file1, delimiter = ";")
        id_all = []
        for row in file_reader:
            id_all.append(row[0])
    id_new = int(max(id_all[1:]))+1        #новый id = +1
    return str(id_new)