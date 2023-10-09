# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_number = [1, 1, 2, 0, -1, 3, 4, 4, 99, 1]

# Пользователь вводит список
# size_list = int(input('Введите размер списка: '))
# for i in range(size_list):
#     list_number.append(int(input(f'Введите {i} элемент списка: ')))

#Рандомный список
# for i in range(size_list):
#     list_number[i] = random.randint(50, -50)
    
print(list_number)
set_namber = set(list_number)
print(len(set_namber))