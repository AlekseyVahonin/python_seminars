# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

n = int(input("Количество монет: "))
coins = []

i = 0
while (i <= n):
    coins.append(random.randint(0, 1))
    print(coins[i], end=" ")
    i += 1
print()

count_one = 0
count_zero = 0
for i in coins:
    if i > 0:
        count_one += 1
    else:
        count_zero += 1

if count_one < count_zero:
    print(count_one)
else:
    print(count_zero)