# -*- coding: utf-8 -*-

# 4 Задание

a = int(input("Расстояние между рядами: "))
b = int(input("Расстояние между дырочками в ряду: "))
L = int(input("Длина свободного конца шнурка: "))
N = int(input("Количество дырочек в каждом ряду: "))
def dlina (a, b, L, N):
    return (2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)
print ("Ответ: ", dlina (a, b, L, N))    

print("\n")