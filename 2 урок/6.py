# -*- coding: utf-8 -*-

# 6 Задание

x1 = int(input("Номер столбца первой клетки: "))
y1 = int(input("Номер строки первой клетки: "))
x2 = int(input("Номер столбца второй клетки: "))
y2 = int(input("Номер строки второй клетки: "))

if ((x1 % 2 != 0) and (y1 % 2 != 0)) or ((x1 % 2 == 0) and (y1 % 2 == 0)):
    one = str ("Черный")
else:
    one = str ("Белый")
if ((x2 % 2 != 0) and (y2 % 2 != 0)) or ((x2 % 2 == 0) and (y2 % 2 == 0)):
    two = str ("Черный")
else:
    two = str ("Белый")

print("Совпадают ли цвета?: ")
if one == two:
    print ("ДА")
else:
    print ("НЕТ")   

print("\n")