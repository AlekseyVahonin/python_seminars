# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
 
x = 1
while x <= s:
    y = 1
    while y <= s:
        if x+y == s and x*y == p:
            print(x,y)
        y += 1
    x += 1

# for i in range(s):
#     for j in range(p):
#         if s == i + j and p == i * j:
#             print(i, j)
