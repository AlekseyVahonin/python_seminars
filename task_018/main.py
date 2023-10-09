# Требуется найти в массиве list_1 
# самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 2, 3, 4, 7, 8, 10]
k = 6

list_2 = list()

for i in list_1:
    list_2.append(abs(k-i))

print(list_1[list_2.index(min(list_2))])