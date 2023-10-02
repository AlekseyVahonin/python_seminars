# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

ticketNumber = int(input("Введите номер билета: "))

firstNumbers = ticketNumber // 100000 + ticketNumber // 10000 % 10 + ticketNumber // 1000 % 10
secondNumbers = ticketNumber // 100 % 10 + ticketNumber // 10 % 10 + ticketNumber % 10


if firstNumbers == secondNumbers:
    print(f"{ticketNumber} -> yes {firstNumbers} {secondNumbers}")
else:
    print(f"{ticketNumber} -> no  {firstNumbers} {secondNumbers}")