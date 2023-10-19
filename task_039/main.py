# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 					Вывод:
# 7					     3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1		

import random
import time


def generate_list(num: int) -> list[int]:
    # list_res = []
    # for _ in range(num):
    #     list_res.append(random.randint(1, 15))
    return [random.randint(1, 1000) for _ in range(num)]


def change_list(lst_a: list, lst_b: list) -> list[int]:
    set_b = set(lst_b)
    list_res = []
    for el in lst_a:
        if el not in set_b:
            list_res.append(el)
    return list_res


def change_list2(lst_a: list, lst_b: list) -> list[int]:
    set_b = set(lst_b)
    # list_res = []
    # for el in lst_a:
    #     if el not in set_b:
    #         list_res.append(el)
    return [el for el in lst_a if el not in set_b]


list1_size = int(input("Enter list1 size: "))
list1 = generate_list(list1_size)
# print(list1)

list2_size = int(input("Enter list2 size: "))
list2 = generate_list(list2_size)
# print(list2)
print("===" * 10)

start_time = time.time()

print(*change_list(list1, list2))

finish_time = time.time()
delta_time1 = finish_time - start_time
print(f"{delta_time1 = }")

start_time = time.time()

print(*change_list2(list1, list2))

finish_time = time.time()
delta_time2 = finish_time - start_time
print(f"{delta_time2 = }")