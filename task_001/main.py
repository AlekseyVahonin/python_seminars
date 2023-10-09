from math import ceil

# За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

speed = int(input('Введите скорость: '))
distance = int(input('Введите растояние: '))

# print(f'Output: {(distans - 1) // speed + 1}' )

# print(f'Output: {ceil((distance - 1) / speed + 1)}')

print(f'Output: {(distance + speed - 1) // speed}')