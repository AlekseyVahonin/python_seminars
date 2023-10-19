# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве выведет количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0				2

import random


def generate_arr(num: int) -> tuple[int]:
    return tuple(random.randint(1, 15) for _ in range(num))


def count_nums(tuple_a: tuple) -> int:
    count = 0
    for i in range(1, len(tuple_a) - 1):
        if tuple_a[i] > tuple_a[i - 1] and tuple_a[i] > tuple_a[i + 1]:
            count += 1
    return count


list1_size = int(input("Enter list1 size: "))
tuple1 = generate_arr(list1_size)
print(tuple1)
print(count_nums(tuple1))

