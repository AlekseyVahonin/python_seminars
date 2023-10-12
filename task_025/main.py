# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# text = "a a a b c a a d c d d"
# list_1 = text.split()
# print(list_1)
# dict_1 = dict()
# for letter in list_1:
#     if letter not in  dict_1:
#         dict_1[letter] = 0
#         print(letter, end=" ")
#     else:
#         dict_1[letter] += 1
#         print(f"{letter}_{dict_1[letter]}", end=" ")

text = "a a a b c a a d c d d"
dict_1 = dict()
for letter in text.split():
    print(letter, end=" ") if letter not in dict_1 else print(f"{letter}_{dict_1[letter]}", end=" ")
    dict_1[letter] = dict_1.get(letter, 0) + 1