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