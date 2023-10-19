# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод:			Вывод:
# 300			220 284

def sum_divisors(num: int) -> int:
    sum_res = 1
    sq_num = num ** 0.5
    if sq_num == int(sq_num):
        sum_res += int(sq_num)
        for div in range(2, int(sq_num)):
            if num % div == 0:
                sum_res += div + num // div
    else:
        for div in range(2, int(sq_num) + 1):
            if num % div == 0:
                sum_res += div + num // div
    return sum_res


def find_pairs(k: int) -> None:
    for num_1 in range(2, k + 1):
        num_2 = sum_divisors(num_1)
        if num_1 == sum_divisors(num_2) and num_1 < num_2 < k:
            print(num_1, num_2)


num_k = int(input("Enter number: "))
find_pairs(num_k)