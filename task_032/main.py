# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 ,
# разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:

# a1 = 2
# d = 3
# n = 4
# На выходе:

# 2 5 8 11

def arithmetic_progression(a1_elem, d_elem, n_elem) -> None:
    for i in range(1, n_elem + 1):
        print(a1_elem + (i-1) * d_elem)


a1 = int(input('Введите первый элемент а1: '))
d = int(input('Введите разность d: '))
n = int(input('Введите количество элементов n: '))

arithmetic_progression(a1, d, n)
