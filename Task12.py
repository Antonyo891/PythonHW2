'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
    а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
    этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''
import random, os
os.system('cls')
firstNumber = random.randint(1,1000)
secondNumber = random.randint(1,1000)
sum = firstNumber+secondNumber
product = firstNumber*secondNumber
print(f'Summa чисел  - {sum}')
print(f'Proizvedenie - {product}')
discriminant = sum**2-4*product
firstNumberKate = int((sum+discriminant**0.5)/2)
print(f'первое число = {firstNumberKate} ({firstNumber}) ')
print(f'второе число = {sum - firstNumberKate} ({secondNumber})')