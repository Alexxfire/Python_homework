# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x1, y1 = int(input('Введите координату X первой точки:')), int(input('Введите координату Y первой точки:'))
x2, y2 = int(input('Введите координату X второй точки:')), int(input('Введите координату Y второй точки:'))
length = ((x2-x1)**2+(y2-y1)**2)**0.5
print(f"Длина отрезка с координатами {x1,y1}; {x2,y2} -> {length}")