# is_in_stock = {
#     "Notes from the Underground": True,
#     "The Stand": False,
#     "The Tempest": False,
#     "Their Eyes Were Watching": True,
#     "A Passage to India": True,
#     "Candide": True,
#     "Ulysses": True,
#     "Great Expectations": False,
#     "One Hundred Years of Solitude": True,
#     "Crime and Punishment": False,
# }
#
# b = is_in_stock.values()
# c = []
# for i in is_in_stock:
#     c.append(i.lower())
# dct = dict(zip(c, b))
#
# book = input("Which book do you want: ").lower().strip()
# if dct.get(book) == True:
#     print("In stock")
# elif dct.get(book) == False:
#     print("Out of stock")
# else:
#     print("We don't know about this book")
# #
# # word = input("write something: ").strip()
# # a = []
# # dct = {}
# # while word != "x" and word != "х":
# #     a.append(word)
# #     word = input("write something: ").strip()
# # print(a)
# # for i in a:
# #     s = a.count(i)
# #     dct[i] = s
# # print(dct)
#
# import random
# import time
# a = map(str, range(1, 101))
# print(*a)
#
# data = {
#     "Ann": {
#         "age": 32,
#         "status": "single",
#     },
#     "Mike": {
#         "age": 30,
#         "status": "single",
#     },
#     "Luke": {
#         "age": 20,
#         "status": "married",
#     },
#     "Nate": {
#         "age": 32,
#         "status": "married",
#     },
#     "Lola": {
#         "age": 37,
#         "status": "married",
#     },
#     "Tom": {
#         "age": 45,
#         "status": "divorced",
#     }}
#
# status1 = {"single": 0, "married": 0, "divorced": 0}
# st = {1: 0, 2: 0, 3: 0}
# age = 0
# age2 = 0
# for i in data.values():
#     print(i)
#     if i["status"] == "single":
#         status1["single"] = (i.get("age") + status1["single"])
#         st[1] += 1
#         age = age + i.get("age")
#         age2 += 1
#     elif i["status"] == "married":
#         status1["married"] = (i.get("age") + status1["married"])
#         age = age + i.get("age")
#         st[2] += 1
#         age2 += 1
#     elif i["status"] == "divorced":
#         status1["divorced"] = (i.get("age") + status1["divorced"])
#         age = age + i.get("age")
#         st[3] += 1
#         age2 += 1
#     else:
#         print("Инвалид эррор")
#
# asa = 1
#
# for a, b in status1.items():
#     print(f"Average {a} person's age is {round(float(b/ st[asa]), 1)}")
#     asa += 1
# asa = 1
# for a, b in status1.items():
#     print(f"{st[asa]} people survey - {a}")
#     asa += 1
#
# print(f"Average age of all interviewed people {round(age/age2, 1)}")


#
# import random
# import time
# a = list(map(str, range(1, 101)))
# random.shuffle(a)
# for i in a:
#     print(i)
#     time.sleep(3)

# import math
#
# nn = input("Прямоугольник, треугольник, круг? ").lower().strip()
# if nn == "прямоугольник":
#     a = int(input("Длинна: "))
#     b = int(input("Ширина: "))
#     print("Площадь равна:", a * b)
# elif nn == "треугольник":
#     a = int(input("Сторона А: "))
#     b = int(input("Сторона B: "))
#     c = int(input("Сторона C: "))
#     # Полу периметр
#     p = (a * b + b * c + a * c) / 2
#     print("Площадь равна:", math.sqrt(p * (p - a) * (a - b) * (p - c)))
# elif nn == "круг":
#     r = int(input("Радиус: "))
#     print("Площадь круга равна:", math.pi * (r ** 2))
#
# lst = map(int, input().split())
# positive = 0
# neg = 1
# min = 0
# max = 0
# for i in lst:
#     if i > 0:
#         positive += 1
#     elif i < 0:
#         neg = neg * i
#     if i < min:
#         min = i
#     elif i > max:
#         max = i
#
# print(f'Количество положительных чисел {positive}')
# print(f'Произведение отрицательных чисел {neg}')
# print(f'Минимальное число {min}')
# print(f'Максимально число {max}')
# #
# n = int(input())
# if not n % 2:
#     print("Простое число")
# while True:
# import random
# dct1 = {"январь": "january", "февраль": "february", "март": "march", "апрель": "april",
#         "май": "may", "июнь": "june", "июль": "july", "август": "august",
#         "сентябрь": "september", "октябрь": "october", "ноябрь": "november",
#         "декабрь": "december"}
# rus = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь",
#        "октябрь", "ноябрь", "декабрь"]
# random.shuffle(rus)
# mistakes = 4
# for i in rus:
#     month = input(f"Месяц  {i} по-английски называется: ").lower().strip()
#     if dct1.get(i) == month:
#         continue
#     while dct1.get(i) != month:
#         print(f"Неверно! Осталось попыток: {mistakes - 2}")
#         month = input(f"Месяц  {i} по-английски называется: ").lower().strip()
#         mistakes -= 1
#         if mistakes == 0:
#             print("Попытки исчерпаны!")
#             break
#         elif dct1.get(i) == month:
#             mistakes = 4
#             break
# print("Конец игры")

# num = int(input())
# matrix = []
# for _ in range(num):
#     matrix.append(list(map(int, input().split())))
# ans = "Yes"
# for i in range(num - 1):
#     for j in range(num - i - 1):
#         if matrix[i][j] != matrix[num - j - 1][num - i - 1]:
#             ans = " No"
#             break
#         if ans == "No":
#             break
# print(ans)
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '*', j, "=", i * j)
#
# print()

#   PIECE OF SHIT THAT DOESN'T WORK
# n = int(input())
# coord = []
# for _ in range(n):
#     coord = list(map(int, input().split()))
#
# first = 0
# second = 0
# third = 0
# fourth = 0
#
# for i in coord:
#     if i[0] > 0 and i[1] > 0:
#         first =+ 1
#     if i[0] < 0 and i[1] > 0:
#         second =+ 1
#     if i[0] < 0 and i[1] < 0:
#         first =+ 1
#     if i[0] > 0 and i[1] < 0:
# #         first =+ 1
#
# Q1, Q2, Q3, Q4 = 0, 0, 0, 0
# for _ in range(int(input())):
#     x, y = [int(i) for i in input().split()]
#     if int(x) > 0 and int(y) > 0:
#         Q1 += 1
#     elif int(x) < 0 and int(y) > 0:
#         Q2 += 1
#     elif int(x) < 0 and int(y) < 0:
#         Q3 += 1
#     elif int(x) > 0 and int(y) < 0:
#         Q4 += 1
# print(Q1, Q2, Q3, Q4)

#
# students = {'Salat': {'math': [5, 5, 4], 'it': [3, 3, 3], 'language': [2, 5, 5]},
#
#             'Damir': {'math': [3, 3, 3], 'it': [5, 5, 2], 'language': [4, 2, 3]},
#
#             'Nursultan': {'math': [5, 5, 2], 'it': [4, 4, 4], 'language': [5, 5, 5]}}
# s = 0
# a = {}
# for i in students:
#     for j in students[i]:
#         d = students[i][j][0] + students[i][j][1] + students[i][j][2] / 3
#         if d > s:
#             s = d
#             a[i] = j
#         else:
#             continue
#     s = 0
# print(a)
# #
# n = map(str, input().split())
# for i in n:
#     if int(i[0]) + int(i[1]) == 10:
#         print(i[0], "+", i[1],"=", int(i[0]) + int(i[1]))

# a = [i for i in range(1, 100)]
#
# b = []
# for i in a:
#     for j in range(2, i -1)
#         if i % j == 0
# print(b)
#
# word = list(input("Write something: "))
# a = len(word) // 2
# n = -1
# n1 = 0
# b = "Ваша строка является палиндромом"
# for i in range(a):
#     if word[n1] == word[n]:
#         n += -1
#         n1 += 1
#         continue
#     elif word[n1] != word[n]:
#         n += -1
#         n1 += 1
#         b = "Ваша строка не является палиндромом"
# print(b)

#
# n = 190187200
# a = []
# for i in range(1, n+1):
#     if n % i == 0:
#         a.append(i)
#     else:
#         continue
# print(len(a))

# number = 190187200
# lst = [1, number]
# for i in range(2, 1 + int(number ** 0.5)):
#     if number % i == 0:
#         lst.extend([number // i, i])
# print(len(sorted(lst)))
# print(int(number ** 0.5))
#
# lenght = float(input("Длинна: "))
# i = False
# while i != True:
#     kuski = float(input("Сколько резать: "))
#     dm = input("m or dc: ")
#     if dm == "dc":
#         kuski = kuski * 0.1
#     if lenght % kuski == 0:
#         print("У вас получилось", int(lenght // kuski), "кусков")
#         i = True
#     elif lenght % kuski != 0:
#         print("У вас получилось", int(lenght // kuski), "кусков и", lenght % kuski, "остаток")
#         lenght = float(input("Длинна: "))
#
# #
# a = int(input("number from 0 to 10: "))
# while 0 < a > 10:
#     print("Insert numbers from 0 to 10 only")
#     a = int(input("number from 0 to 10"))
# # #
# for i in range(4):
#     b = int(input("Gues the number from 0 to 10: "))
#     if a == b:
#         print("You win")
#         break
#     elif i < 2 and a != b:
#         print("Try again")
#     if i == 2:
#         print("game over")
#         break

# exam_results = {
#     'Ann': {'grade': 4,},
#     'Mike': {'grade': 4,},
#     'Luke': {'grade': 5,},
#     'Nate': {'grade': 3,},
#     'Lola': {'grade': 4,},
#     'Tom': {'grade': 5,},
#     'Bob': {'grade': 3}}
#
# for i in exam_results:
#     if exam_results[i]['grade'] == 5:
#         exam_results[i]["grand"] = True
#     if exam_results[i]['grade'] < 5:
#         exam_results[i]["grand"] = False
# print(exam_results)
#
# a = int(input())
# i = 1
# while i != a + 1:
#     print("*" * i)
#     i += 1
#
# a = int(input())
# i = 1
# j = 1
# while i < a:
#     while j <= i:
#         print("*", end="")
#         j +=1
#     j = 0
#     i += 1
#     print("")
# import time
# f1, f2 = 1, 1
# for i in range(int(input())):
#     print(f1)
#     f1, f2 = f2, f1 + f2
#     time.sleep(0.1)

# a = int(input())
# fac = 1
# while fac != a:
#     fac *= a
#     print(fac)
#     fac += 1

# a = int(input())
# fac = 1
# while a > 1:
#     fac *= a
#     a -= 1
#     print(fac)
#
a = range(2, 100)
b = [2, 3, 5, 7]
for i in a:
    if i % b[0] == 0:
        print("2")
        continue
    elif i % b[1] == 0:
        print("3")
        continue
    elif i % b[2] == 0:
        print("5")
        continue
    elif i % b[3] == 0:
        print("7")
        continue
    else:
        b.append(i)
print(b)

# n = int(input())
# rev = 0
# while n != 0:
#     r = n % 10
#     print(r)
#     rev = rev * 10 + r
#     print(rev)
#     n = n // 10
#     print(n)
# print(rev)

# a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]
# c = list(set(a).intersection(set(b)))
# print(c)
# c = [i ** 3 for i in c]
# for i in c:
#     if i < 0:
#         ind = c.index(i)
#         c[ind] = c[ind] * -1
#     if type(i) == float:
#         ind = c.index(i)
#         c[ind] = int(c[ind])
#     else:
#         continue
# print(c)
# #
# name = input("Name: ")
# mail = input("Email: ")
# pswd = input("Password: ")
# while True:
#     l = len(mail)
#     pswd_digit = False
#     pswd_up = False
#     pswd_low = False
#     for i in pswd:
#         if i.isupper():
#             pswd_up = True
#         if i.isdigit():
#             pswd_digit = True
#         if i.islower():
#             pswd_low = True
#         else:
#             continue
#
#     if name.isalpha() == False:
#         print("Неверное имя")
#     if mail[l - 9: l] != "gmail.com":
#         print("Неверный Email", mail[-10: 0])
#     if len(pswd) < 8:
#         print("Неверный пароль")
#     elif pswd_digit == False or pswd_up == False or pswd_low == False:
#         print("Пароль должен состоять из букв верхнего, нижнего регистра и цифр")
#     else:
#         print("Вы успешно зарегистрировались")
#         break
#     name = input("Name: ")
#     mail = input("Email: ")
#     pswd = input("Password: ")
# print(f'Ваше имя: {name}')
# print(f'Ваша почта: {mail}')
# print(f"Ваш пароль: {'*' * l}")

# question = input()
# bot = {"Кто ты?": "Я программа", "Что делаешь?": "Работаю",
#        "Как это работает?":"Как то так", "Где ты?":"У тебя на компе"}
# while question != "q":
#     print(bot.get(question))
#     question = input()
#
#
# num = input("Number: ")
# action = input("Action: ")
# solution = "0"
# while num != "" or num != "":
#     if not num.isdigit():
#         print("I say number, not letters")
#     elif action != "+" and action != "-" and action != "*" and action != "**" and action != "/" and action != "//":
#         print("Action like + - / // * **")
#     else:
#         solution = str(solution) + str(action) + str(num)
#         solution = eval(solution)
#         print(solution)
#     num = str(input("Number: "))
#     action = str(input("Action: "))

# from string import ascii_lowercase, ascii_uppercase
# print(list(ascii_lowercase))
# uppers = list(ascii_uppercase)
# print(uppers)