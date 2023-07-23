#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import os
os.system('cls')
power = -1
number = int(input("Vvedite 4islo "))
while 2**power < number:
    power+=1
    if 2**power <=number:
        print (power, end=' ')
print()