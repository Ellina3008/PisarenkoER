# -*- coding: utf-8 -*-

#4 Задание:
print("4 Задание: ")

sec = int(input("Введите секунды: "))
d = sec // 86400
h = (sec-d*86400) // 3600
m = (sec-h*3600) // 60
s = sec % 60
print(d, 'суток',h,'час',m,'мин',s,'сек')