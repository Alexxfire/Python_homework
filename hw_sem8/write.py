import user
import csv
import output
import os
import datetime

now = datetime.datetime.now()
now_str = str(now.strftime("%d-%m-%Y %H-%M-%S"))

def Ocenka(result):                 #выставляем оценку
    predmet = user.Predmet()
    print('БЫЛО ->')
    row_write = output.Show_ocenki_predmet(predmet,result)
    ocenka_new = user.Ocenka_verna()
    Ocenka_write(predmet,result, row_write, ocenka_new)

def Ocenka_write(predmet,result, row_write, ocenka_new):      #записываем оценку
    global now_str
    with open("ocenki.csv", encoding='cp1251') as file1:
        file_reader = csv.reader(file1, delimiter = ";")
        new_file = []
        for row in file_reader:
            new_file.append(row)                                
        for j in range(len(new_file[3])-1, 1, -1):        #ищем первую оценку с конца
            if new_file[row_write][j].isdigit():
                new_file[row_write][j+1] = ocenka_new
                break
            elif j == 2:
                new_file[row_write][j] = ocenka_new
        row1 = list(filter(lambda e: e.isdigit(), new_file[row_write]))
        row1 = list(map(int,row1[1:]))      
        print(f'СТАЛО -> \n{" ".join(new_file[row_write])} : средняя оценка {"0" if len(row1)==0 else round(sum(row1)/len(row1),1)}')
    os.rename('ocenki.csv', 'ocenki_old_'+now_str+'.csv')  
    with open("ocenki.csv", 'a', newline='') as file_fin:
        file_writer = csv.writer(file_fin, delimiter = ";")    
        for i in range(len(new_file)):
            file_writer.writerow(new_file[i])


def Add():                              #добавляем ученика
    new_uchenic = user.New_uchenik()
    Write_school(new_uchenic)
    Write_ocenki(new_uchenic)
    

def Write_school(new_uchenic):         #ученика записываем в школу
    global now_str
    new_file = []
    with open("school.csv", encoding='cp1251') as file_new_uch:
        file_reader = csv.reader(file_new_uch, delimiter = ";")
        for row in file_reader:
            new_file.append(row)
    new_file.append(new_uchenic)
    #print(new_file)
    os.rename('school.csv', 'school_old_'+now_str+'.csv')  
    with open("school.csv", 'a', newline='') as file_fin:
        file_writer = csv.writer(file_fin, delimiter = ";")    
        for i in range(len(new_file)):
            file_writer.writerow(new_file[i])
            
        
def Write_ocenki(new_uchenic):          #ученика записываем в предметы/оценки
    global now_str
    new_file = []
    with open("ocenki.csv", encoding='cp1251') as file_new_uch:
        file_reader = csv.reader(file_new_uch, delimiter = ";")
        for row in file_reader:
            new_file.append(row)    
        row1_new = ['']*12
        row1_new[0] = new_uchenic[0]
        row1_new[1] = 'Русский'
        new_file.append(row1_new)
        row2_new = ['']*12
        row2_new[0] = new_uchenic[0]
        row2_new[1] = 'Математика'
        new_file.append(row2_new)    
    os.rename('ocenki.csv', 'ocenki_old_'+now_str+'.csv')  
    with open("ocenki.csv", 'a', newline='') as file_fin:
        file_writer = csv.writer(file_fin, delimiter = ";")    
        for i in range(len(new_file)):
            file_writer.writerow(new_file[i])