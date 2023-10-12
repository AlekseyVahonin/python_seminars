# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

# На выходе:
# 3 5

set_1 = set((var2.split()))
set_2 = set((var3.split()))

set_3 = sorted(set_1.intersection(set_2))
for item in set_3:
    print(item, end=' ')