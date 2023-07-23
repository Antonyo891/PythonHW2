'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть'''
import random
import os
os.system('cls')
numberOfCoin = random.randint(1,40)
print ("+ - орел")
print ('- - решка')
heads = 0
tails = 0
print(f"{numberOfCoin} монет лежит на столе")
for _ in range(numberOfCoin):
    up = random.choice(['heads','tails'])
    if up == 'heads':
        heads +=1
        print('+',end=' ')
    else: 
        tails +=1
        print('-', end = ' ')
print(';')
min = heads
if heads>tails:
    min = tails
print (f"Чтобы все {numberOfCoin} монет лежали одной стороной вверх нужно перевернуть {min} монет")