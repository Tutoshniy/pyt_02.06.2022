# # Задание 1: Найти НОК двух чисел
# def max_common_divisor(a, b):
#     while b != 0:
#         temp = b
#         b = a % b   #Алгоритм Евклида
#         a = temp
#     return a
# def min_common_divisor(a, b):
#     return (a * b) / max_common_divisor(a, b)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if b > a:
#     a, b = b, a
# nok = int(min_common_divisor(a, b))
# print(f"Наименьшее общее кратное {a} и {b} равно {nok}.")

# #Задание 2: Вычислить число Пи c заданной точностью d
# import math
# import decimal
# def get_count(number):
#     s = str(number)
#     if '.' in s:
#         return abs(s.find('.') - len(s)) - 1
#     else:
#         return 0

# d = float(input("Укажите точность: "))
# print(round(math.pi-d, get_count(d)))

# #Задание 3 Составить список простых множителей натурального числа N
# a = int(input("Введите число: "))
# prim = []
# def is_primal(chislo):
#     k = 0
#     for i in range(2, chislo//2 + 1):
#         if (chislo % i == 0):
#             k = k+1
#     if (k <= 0):
#         prim.append(chislo)
# for i in range(1,a+1):
#     if a%i==0:
#         is_primal(i)
# print(prim)

# #Задание 4 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# a = [1, 2, 3, 5, 1, 5, 3, 10]
# nuzhiy = []
# a = sorted(a)
# nuzhiy.append(a[0])
# for i in range(len(a)-1):
#     if a[i] != a[i+1]:
#         nuzhiy.append(a[i+1])
# print(nuzhiy) 

#Задание 5 Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
import random

chisla = []
with open('file.txt', 'w') as data:
    for i in range(random.randint(3,10)):
        rand_num = random.randint(10,100) #можно было сделать легче, но это для проверки
        data.write(f"{rand_num}\n")
        print(rand_num, end= ' ')
with open('file.txt', 'r') as data:
    for line in data:
        line.replace('\n','')
        if int(line)%2!=0:
            chisla.append(line)
with open('file.txt', 'w') as data:
    for i in range(len(chisla)):
        data.write(chisla[i])

            
