# for i in range(5):
#     print("Python")
#
# for i in "Python":
#     print(i)

# lst1 = ['1', '2', '3', '4', '5']
# lst2 = ['a', 'b', 'c', 'd', 'e']
# for i in lst1:
#     for j in lst2:
#         print(i + j)

# age = int(input("How old are you? "))
# if age < 7:
#     print("Ходишь в детсад")
# elif 18 <= age <= 23:
#     print("В какой школе учишься")
# elif 60 <= age <= 90:
#     print("Уже не работаешь")
# elif age > 90:
#     print("Долгожитель")
# else:
#     print("Работаешь")


# st = 'abracad5bra'
# for i in st:
#     if not i.isalpha():
#         print(i)
#
# st = '32ey.5yhsf$h%owe82038e-3q0dwaefsfdgfhyfWfd9fG'
# for i in st:
#     if i.isdigit() and int(i) > 8:
#         print(i)
#         break
#
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
#
# # 2-й способ вывода
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         print(lst[i][j], end=' ')
#     print()
# print()

# n, m = int(input()), int(input())
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         temp = input()
#         matrix[i].append(temp)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()

# st = input()
# sp = []
#
# for i in st:
#     if i.isalpha():
#         sp.append(i)
# print(sp)
#
# sp2 = [i for i in st if i.isalpha()]
# print(sp2)
#
# list1 = ['а', 'б', 'в', 'г', 'д']
# list2 = [1, 2, 3, 4, 5]
# for i, j in zip(list1, list2):
#     print(i + str(j))

# list1 = ['а', 'б', 'в', 'г', 'д']
# list2 = [1, 2, 3, 4, 5]
# for i in range(len(list1)):
#     print(list1[i], list2[i])
#
# my_list = ['хард-рок', 'хэви-метал', 'хип-хоп', 'рэп', 'панк-рок']
# for i, j in enumerate(my_list):
#     print(i, j)

# lsg = [3, 5, 7, -2, -4, 6, 2, -3, 6]
# k = 0
# for i in lsg:
#     if i < 0:
#         k += 1
# print(k)

# lst = list(map(int, input().strip().split()))
# n = 0
# for i in lst:
#     print(i)
#     if i != 0:
#         n += i
#     else:
#         break
# print(n)

# n = int(input())
# a = 0
# while n != 0:
#     a += n
#     n = int(input())

# import random
# lst = [i for i in range(random.randint(5, 500))]
# print(lst)
# while True:
#     if not lst:
#         break
#     print(lst.pop())
#
# n = int(input())
# i = 2
# while True:
#     if n %2 == 0:
#         break
#     i += 1
# print(i)

# text = "Введите любое слово: "
# text += "\n или введитн exit"
#
# active = True
# while active:
#     message = input(text)
#     if message == "exit":
#         active = False
#     else:
#         print(message)

# sp = []
# while len(sp) < 5:
#     num = int(input())
#     if num == 50 or 90 <= num <= 120:
#         continue
#     sp.append(num)
# print(sp)
#
# import random
# lst = [i for i in range(random.randint(5, 500))]
# while len(lst) > 1:
#     print(lst.pop())
# else:
#     print("List is empty")

# n = int(input())
# while True:
#     if n == 0:
#         break
#     elif n > 50 or n <= -50:
#         break
#     elif n % 2 == 0:
#         break
#     print(n / 5)
#     n = int(input())
#
# while True:
#     for i in range(5):
#         print(i)
#
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# for i in range(10):
#     print(i)

# n = int(input())
# while True:
#     if n == 0:
#         break
#     print(n**2)
#     n = int(input())
#
# language = "russian"
# daytime = "morning"
# if language == "english":
#     if daytime == "morning":
#         print("Good morning")
#     else:
#         print("good evening")
# else:
#     if daytime == "morning":
#         print("Доброе утро")
#     else:
#         print("Добрый вечер")

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
#
# summa = 0
# prof = 1
# for i, j in enumerate(lst):
#     for num in j:
#         summa += num
#         prof *= num
#     print(f'Подсписок {i}: сумма чисел = {summa}, произведение = {prof}')
#     summa = 0
#     prof = 1

# a = "12"
# b = "122"
# c = "*"
# a = a + c + b
# print(eval(a))

a = "*&"
print(a.isalnum())