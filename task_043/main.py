# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:			Вывод:
# 1 2 3 2 3			2

import random


def count_pairs(tuple_a: tuple) -> int:
    count = 0
    for i in range(len(tuple_a) - 1):
        for j in range(i + 1, len(tuple_a)):
            if tuple_a[i] == tuple_a[j]:
                count += 1
    return count


def count_pairs1(tuple_a: tuple) -> int:
    count = 0
    for i in range(len(tuple_a) - 1):
        count += tuple_a[i + 1:].count(tuple_a[i])
    return count


num = int(input("Enter number: "))
tuple1 = tuple(random.randint(1, 10) for i in range(num))
print(tuple1)
print(count_pairs1(tuple1))