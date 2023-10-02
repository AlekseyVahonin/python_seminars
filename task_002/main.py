# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите 3-х значное число: "))

if number < 0:
    number *= -1

if number > 999 or number < 100:
    print("Число не 3-х значное")
else:
    print(f'{number} -> {number // 100 + number % 100 // 10 + number % 10}')