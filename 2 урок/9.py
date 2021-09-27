# -*- coding: utf-8 -*-

# 9 Задание

n = int(input("Первая сторона шоколадки: "))
k = int(input("Вторая сторона шоколадки: "))
m = int(input("Оставшаяся часть: "))
if (n == k or k % n == 0 and k <= n * m - n) or (m == k or k % m == 0 and k <= n * m - m):
    print("ДА")
else:
    print("НЕТ")

print("\n")