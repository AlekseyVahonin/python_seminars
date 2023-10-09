# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# import random

# n = int(input("Введите число: "))
# max_num = 1
# min_num = 1000000
# for i in range(n):
#     num = random.randint(1, 20)
#     print(num, end=" ")    
#     if num < min_num:
#         min_num = num
#     if num>max_num:
#         max_num=num
# print()
# print(f'минимальное число {min_num}\nмаксимальное число {max_num}')

#Второй вариант

import random

n = int(input("Введите число: "))
num = random.randint(1, 20)
max_num = num
min_num = num
#print(num, end=" ")
for _ in range(n):
    num = random.randint(1, 20)
    print(num, end=" ")    
    if num < min_num:
        min_num = num
    if num>max_num:
        max_num=num
print()
print(f'минимальное число {min_num}\nмаксимальное число {max_num}')