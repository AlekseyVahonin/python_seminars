# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def revers_nums(count_nums):
    if count_nums == 0:
        return ''
    k = input('Введите число: ')
    return  revers_nums(count_nums - 1) + ' ' + k

nums = int(input('Введите количество чисел '))
print(revers_nums(nums))