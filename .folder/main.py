#. Напишите программу, которая на вход принимает два 
#числа и проверяет, является ли второе число квадратом 
#первого.
#a = 5; b = 25 -> да 
#a = 9; b = -3 -> нет
#a = -3 b = 0 -> нет
#numder1 = int(input("Введите число: "))
#numder2 = int(input("Введите предполагаемый квадрат числа: "))
#if numder1**2 == numder2:
 #   print(f"Число {numder2} является квадратом {numder1}")
#else:
#    print(f"Число {numder2} не является квадратом {numder1}")

# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди
# введённых чисел те, которые кратны трём.
#number=1
#while number!=0:
 #   number= float(input('Number? '))
  #  print(number%3==0)
#print('End!')

#Напишите программу, которая будет на вход
#принимать число N и выводить числа от -N до N
#num = int(input('Введите любое число: '))
 #for value in range(-num, num + 1):
 #   print(value)


#Напишите программу, которая будет принимать на вход дробь 
#и показывать первую цифру дробной части числа.
#a = float(input())
#print(int(a * 10) % 10)

#Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.
#	10 -> 10 (чётный), 5(нечётный), 2 (чётный), 
#number = int(input('Введите число: '))

#print('Цикл for:')
#for i in range(1, number+1):
 #   if number % i == 0:
  #      if i % 2 == 0:
   #         print(f'{i} чётное')
    #    else:
     #       print(f'{i} нечётное')

#Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.
#def zadacha2():
 #   for x in range(0,2):
  #      print(x)

#zadacha2
#for x in range(2):
 #       for y in range(2):
  #          print(f'{x} {y} {x==0 or y==1}')

#Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.rfg
#sostring = input()
#fistring = input()
#b = 0
#e = len(fistring)
#count = 0
#while e < len(sostring) + 1:
  #  if sostring[b:e] == fistring:
   #     count += 1
  #  b += 1
 #   e += 1
#rint(count)

#Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
#def zadacha1():
#  numbers =[]
 # n= int(input('Введите число:'))
 # for el in range(n):
 #   numbers.append((-3)**el)
 # print(numbers)
#def subtask5(num: int):
 #   count = 0
  #  for i in range(1, num+1):
   #     if num % i == 0:
    #        count += 1    
   # return count
#def task5():
 #   for i in range(1,10000):
  #      if subtask5(i) == 10:
   #         print(f'{i}\t', end='')
#Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.
#def zadacha4():
 #   count = 0
  #  for num in range(1, 10001):
   #     count_div = 0
    #    for div in range(1, num+1):
     #       if num % div == 0:
      #          count_div += 1
       # if count_div == 10: 
        #    count += 1
         #   print(num)
    #print(f'Кол-во чисел у которых 10 делителей = {count}')
# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.
# import random 

# length= 7
# numbers =[0]*length

# for index in range(length):
#     numbers[index]=random.randint(0,10)
# print(numbers)
# numbers =[random.randint(0,10) for el in range(length)]
# print(numbers)
# sum =0 
# for index in range(length):
#     sum += numbers[index]
# print(f"сумма всех элементов {sum}")
# if sum % 2==0 :
#     print("Сумма ч")
      
# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# import random
# length = 30
# numbers = [random.randint(0, 25) for el in range(length)]
# sum1 = 0
# sum2 = 0
# for i in range(15):
#     sum1 += numbers[i]
# for j in range(16, 30):
#     sum2 += numbers[j]

# if sum1 > sum2:
#     print('Осадков больше в первой половине июня')
# else:
#     print('Осадков больше во второй половине июня')

# Задача 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.
# form = dict(Имя = input('Ваше имя: '), Возраст = input('Ваш возраст: '), Хобби = input('Ваше хобби: '), Любимое_животное = input('Ваше любимое животное: '))
# print()
# for key, value in form.items():
#         print("{0}: {1}".format(key,value))

# Задача 3. Напишите скрипт генератора паролей 
# заданной длины, состоящих из латинских букв и 
# чисел.
# def Task3(length):
#     letters_and_digits = string.ascii_letters + string.digits
#     password = ''.join(random.sample(letters_and_digits, length))
#     print(password)

# Task3(16)
# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 
# рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу
# позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». 
# Определите сумму чека
# dict = {'Ручка':5, 'карандаш':3, 'ластик':4}
# sum = 0
# flag = True
# while flag:
#     code = input('Введите наименование: ')
#     if code in dict:
#         sum += dict[code]
#     elif code == 'стоп':
#         flag = False          
# print(sum)

# Задача 0 Создайте кортеж. Запишите в него 10 случайных чисел
# Задача 1 pоздайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.
# import random
# def change_element(numbers, index):
#     return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

# numbers = tuple(random.randint(1, 100) for _ in range(10))
# index = 2

# print(numbers)
# numbers = change_element(numbers, index)
# print(numbers)
# print(type(numbers))

# Задача 2:
# На вход подаются два числа. Напишите метод, который вернёт 
# сумму, разность, произведение и частное этих чисел.
# import random
# def change_element(numbers, index):
#     return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

# def calculate(n1, n2):
#     return n1 + n2, n1 - n2, n1 * n2, n1/ n2

# def zadacha1():
#     numbers = tuple(random.randint(1, 100) for _ in range(10))
#     index = 2

#     print(numbers)
#     numbers_new = change_element(numbers, index)
#     print(numbers_new)


# def zadacha2():
#     num_f = 9
#     num_s = 3

#     summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)
#     print(summ, raznost, umnozhenie, delenie)
# Задача 3:
# Сгенерируйте список случайных чисел от 1 до 20, 
# состоящий из 10 элементов. Удалите из списка 
# дубликаты уже имеющихся элементов. Определите, 
# сколько элементов было удалено.
# import random
# number = [random.randint(1, 20) for _ in range(10)]
# new_number = set(number)
# res = len(number) - len(new_number)
# print(res)
# Задача 4. Актёров разделили на списки по трём качествам 
# «умные», «красивые», «сильные». На главную роль нужен 
# актёр обладающий всеми тремя качествами. Определите, 
# сколько есть претендентов на главную роль.
# beuty = set("Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
# clever = set("Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад".split())
# strong = set("Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад".split())
# print(f"Актеры обладающие всеви тремя качествами : {beuty and clever and strong}")

# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. Заполните список случайным образом числами от 1 до 100.
# def Task1():
#     num_list = [random.randint(1, 100) for _ in range (15)]
#     result = list(filter(lambda x: x % 5 == 0, num_list))
#     print(num_list)
#     print(result)
# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.
# number = input("Введите четырехзначное число: ")
# if len(number) != 4:
#         print("Вы ввели неправильное число")
# else:
#         digits = list(
#                         map(
#                             lambda x: int(x) + 10, number))
#         print(digits)
# def zadacha2():
#     animals = ['010100001100001001010011001011000000',
#                 '000001011100001011',
#                 '001011001111010011',
#                 '010010010011001111010001001111000111',
#                 '001100000101000010',
#                 '001011010001001111001100001001001011',
#                 '001101010100001100',
#                 '000001000000010001010010010100001011',
#                 '000011000101010000000000010001000100',
#                 '010010001111001101',
#                 '010010001111000001000000001011000000',
#                 '011000001001000111']
    
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     alphabet = list(alphabet)
#     d = {}
#     for i in range(len(alphabet)):
#         d[ToBinary(i)] = alphabet[i]
#     print(d)

#     result = list(map(lambda x: [d[x[i:i+6]] for i in range(0, len(x), 6)], animals))
#     result = list(map(lambda x: ''.join(x), result))
#     print(result)
#     animals_list = [''.join(alphabet[int(animal[x: x + 6], 2)] for x in range(0, len(animal), 6)) for animal in animals]

# def ToBinary(num):
#     result = ''
#     while num > 0:
#         result = str(num % 2) + result
#         num //= 2
#     return '0' * (6 - len(result)) + result

# def decoder(code):
#     animal = [code[i:i+6] for i in range(0, len(code), 6)]
#     print(animal)
# Задача 1. Дан список случайных элементов. 
# Проверьте, что все его элементы уникальны
# N = [1,2,4,45,6,7,8,45,7,45]
# setN = set(N)
# if len(setN) != len(N):
#         print(f'элементы списка НЕ уникальны')
# else:
#         print(f'все элементы списка не уникальны')
# Задача 2. Даны два случайных пятизначных числа. 
# Определить, состоят ли они из одних и тех же цифр
# import random
# import collections

# def Task2():
#     num1 = [random.randint(1, 9) for _ in range(5)]
#     num2 = [random.randint(1, 9) for _ in range(5)]
#     print(num1)
#     print(num2)
#     if collections.Counter(num1) == collections.Counter(num2):
#         print('Cостоят из одних цифр')
#     else: print('Не состоят из одних цифр')
# Задача 3. Напишите программу вычисления арифметического 
# выражения заданного строкой. Используйте операции +,-,/,*. 
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких 
# действий;
# в) Решите задачу средствами python.
expr = "2+2"
result = int(expr.split("+")[0]) + int(expr.split("+")[1])
print(result)








