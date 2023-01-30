import csv


def Show_ocenki(result):                    #показываем оценки, ср.оценку 
    with open("ocenki.csv", encoding='cp1251') as file1:
        file_reader = csv.reader(file1, delimiter = ";")
        for row in file_reader:
            #print(row)
            for i in range(0, len(result)):
                if result[i][0] == row[0]:
                    row1 = list(filter(lambda e: e.isdigit(), row))
                    row1 = list(map(int,row1[1:]))                    
                    print(f'{" ".join(result[i])} : {" ".join(row[1:])} : средняя оценка {"0" if len(row1)==0 else round(sum(row1)/len(row1),1)}')


def Show_ocenki_predmet(predmet,result):          #показываем оценки по предмету, ср.оценку
    with open("ocenki.csv", encoding='cp1251') as file1:
        file_reader = csv.reader(file1, delimiter = ";")
        count = 0
        for row in file_reader:
            for i in range(0, len(result)):
                if result[i][0] == row[0] and predmet == row[1]:   #если уникальный номер и предмет совпадают
                    row1 = list(filter(lambda e: e.isdigit(), row))
                    row1 = list(map(int,row1[1:]))                    
                    print(f'{" ".join(result[i])} : {" ".join(row[1:])} : средняя оценка {"0" if len(row1)==0 else round(sum(row1)/len(row1),1)}')        
                    count1 = count
            count += 1
        return count1