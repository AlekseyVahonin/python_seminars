# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

n = int(input("Введите число "))

max_pos_num = 0
count = 0
for _ in range(n):
    num = random.randint(-50, 50)
    print(num, end=" ")
    if num > 0:
        count = count+1
        # max_pos_num = max(max_pos_num, count)
        if max_pos_num < count:
            max_pos_num = count
    else:
        count = 0

print()
print(max_pos_num)
