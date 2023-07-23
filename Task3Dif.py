'''задача 3 необязательная
Перечислить все положительные делители некоторых целых чисел.   арианты посложнее: 23436, 190187200, 380457890232.
Помогите ей (при помощи функции all_divisors(number), которую напишете сами).Постарайтесь найти самое оптимальное решение.
Результат представьте в виде списка (не забудьте отсортировать по возрастанию).'''
import os, random, time
time1 = time.time()
os.system('cls')
def all_divisors (number):
    divisors = [1,number]
    divisor = 2
    i=1
    temporary = number
    while divisor < temporary:
        if number%divisor == 0:
            divisors.insert(i,divisor)
            divisors.insert(len(divisors)-(i),number//divisor)
            temporary = number//divisor
            i+=1
        divisor+=1
    return divisors
number = random.randint(1,100000)
print(f'Делители числа {number} - {all_divisors(number)}')
print(f'Делители числа 23436 - {all_divisors(23436)}')
print(f'Делители числа 190187200 - {all_divisors(190187200)}')
print(f'Делители числа 380457890232 - {all_divisors(380457890232)}')
print(f"Время выполнения кода - {time.time()-time1} секунд")
