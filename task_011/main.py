# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6 

f_res = int(input("Введите натуральное число >1: "))
f1 = 1
f2 = 2
i = 4
while f2+f1 <= f_res:
    f = f1 + f2
    f1 = f2
    f2 = f
    # f1, f2 = f2, f1+f2
    i += 1
print(i)