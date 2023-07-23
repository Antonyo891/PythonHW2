'''задача 1 сложная необязательная 
Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.'''
import random, os
os.system('cls')
number = float(input("Vvedite 4islo "))#random.randint(1,99999)/10**random.randint(1,4)
print(number)
temporaryNumber = number
while temporaryNumber%1 != 0:
    temporaryNumber*=10
    print(temporaryNumber)
sum=0
while temporaryNumber/10>0:
    sum=sum+int(temporaryNumber%10)
    temporaryNumber/=10
print(sum)
