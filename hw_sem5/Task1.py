#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

start_string = 'АБВ 2а фыыдлх абв, вба, Зщышф вабву ффлжв абВ!'  #со знаками припинания

#пример из семинара удаляет знаки препинания после абв
fin_string1 = ' '.join(list(filter(lambda e: 'абв' not in e.lower(), start_string.split())))
print(fin_string1)

#мой вариант, не удаляющий знаки препинания 
import re
fin_string2 = re.split(r'\b', start_string)  #разделение с учетом знаков препинания
fin_string2 = ''.join(list(filter(lambda e: 'абв' not in e.lower(), fin_string2)))
print(fin_string2)