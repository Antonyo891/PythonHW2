'''задача Де моргана необязательная Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (не X и Y и Z = не X или не Y или не Z) для всех значений предикат(true false).
теперь надо проверить ее практически в цикле 100 раз прогоняем каждый раз генерируем случайное количество 
предикат от 3 до 15 и конечно со случайным булевым значением и засекаем общее время выполнения программы 
юзаем библиотеки random и time предикаты НЕ ЗАДАЕМ как целое число!'''
import os, random, time, decimal
os.system('cls')
from decimal import Decimal
afterDecimalPoint = Decimal("0.1")
afterDecimalPoint1 = Decimal("0.01")
for _ in range (100):
    x = random.randint(3,15)*random.choice([afterDecimalPoint,afterDecimalPoint1])
    y = random.randint(3,15)*random.choice([afterDecimalPoint,afterDecimalPoint1])
    z = random.randint(3,15)*random.choice([afterDecimalPoint,afterDecimalPoint1])
    number = random.randint(3,15)*random.choice([afterDecimalPoint,afterDecimalPoint1])
    predicata1 = number!=(x and y and z)
    predicata2 = (number!=x or number!=y or number!=z)
    if predicata1==predicata2:
        print(predicata1==predicata2, end='||')
    else:
        print()
        print(f'number = {number}, x = {x}, y = {y}, z = {z}',predicata1,predicata2)