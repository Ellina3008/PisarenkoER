# -*- coding: utf-8 -*-

# 3 Задание

n = int(input("Введите количество минут: "))
hours = n % (60 * 24) // 60
minutes = n % 60
print("Часов: ", hours, "Минут: ", minutes)

print("\n")