# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.

# Пример

# На входе:

list_1 = [-5, 9, 0, 20, -1, -2, 1, 20, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 20]
# min_number = 0
# max_number = 10
# На выходе:

# 1 2 3 6 7 9 10 11 13 14 16 19

def range_index_list(lst:list, min:int, max:int) -> None:
    for i in range(len(lst)):
        if lst[i] >= min_number and lst[i] <= max_number:
            print(i)


min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))

range_index_list(list_1, min_number, max_number)