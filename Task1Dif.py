'''задача 1 сложная необязательная 
Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.'''
import random, os, decimal
os.system('cls')
number = random.randint(1,9999999)
from decimal import Decimal
afterDecimalPoint = Decimal("0.1")
afterDecimalPoint1 = Decimal("0.01")
afterDecimalPoint2 =Decimal("0.001")
afterDecimalPoint3 = Decimal("0.0001")
number = number*random.choice([afterDecimalPoint,afterDecimalPoint1,afterDecimalPoint2,afterDecimalPoint3])
print(number)
temporaryNumber = number
while temporaryNumber%1 != 0:
    temporaryNumber*=10
    sum=0
while int(temporaryNumber)/10>0:
    sum=sum+int(temporaryNumber%10)
    temporaryNumber/=10
print(f'Summa cifr chisla {number} = {sum}')
