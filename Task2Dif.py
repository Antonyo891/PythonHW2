'''задача Де моргана необязательная Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (не X и Y и Z = не X или не Y или не Z) для всех значений предикат(true false).
теперь надо проверить ее практически в цикле 100 раз прогоняем каждый раз генерируем случайное количество 
предикат от 3 до 15 и конечно со случайным булевым значением и засекаем общее время выполнения программы 
юзаем библиотеки random и time предикаты НЕ ЗАДАЕМ как целое число!'''
import os, random, time
time1 = time.time()
os.system('cls')
for _ in range (100):
    predicat1 = "not("
    predicat2 = "not "
    numberOfPredicat = random.randint(3,15) 
    for i in range(numberOfPredicat+1):
        from random import choice
        temporary = choice([True,False])
        if i == numberOfPredicat:
            predicat1 = predicat1 + str(temporary) + ")" 
            predicat2 = predicat2 + str(temporary)
        else:
            predicat1 = predicat1 + str(temporary) + '+'
            predicat2 = predicat2 + str(temporary) + " or not "
    
    predicat1 = bool(predicat1)
    predicat2 = bool(predicat2)
    print (predicat2==predicat1, end=' , ')
print()
print(f"Время выполнения кода - {time.time()-time1} секунд")
