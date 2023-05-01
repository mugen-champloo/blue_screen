#
# def username_generator():
#     from random import randint
#     name = input("Enter your name: ").loweer
#     surname = input("Enter your suraname: ")
#     print("@" + surname + "_" + name + "_" + str(randint(1000, 9999)))
# username_generator()

#
# def my_netflix(full_price, discount_plans, clients):
#     a = 0
#
#     for i in clients:
#         for j in discount_plans:
#             if clients[i]["discount_plan"] == j:
#                 a = a + full_price - full_price * discount_plans[j]
#             else:
#                 continue
#     return a

#
# full_price1 = 100.0
# discount_plans1 = {
#     'regular': 0,
#     'student': 0.15,
#     'pensioner': 0.25}
# clients1 = {
#     'Ann': {'discount_plan': 'regular'},
#     'Mike': {'discount_plan': 'regular'},
#     'Luke': {'discount_plan': 'pensioner'},
#     'Nate': {'discount_plan': 'regular'},
#     'Lola': {'discount_plan': 'student'},
#     'Tom': {'discount_plan': 'regular'},
#     'Bob': {'discount_plan': 'student'},
#     'Rick': {'discount_plan': 'regular'},
#     'Morty': {'discount_plan': 'regular'},
#     'Beth': {'discount_plan': 'pensioner'},
#     'Jerry': {'discount_plan': 'regular'},
#     'Summer': {'discount_plan': 'pensioner'}}
#
# print(my_netflix(full_price=full_price1, discount_plans=discount_plans1, clients=clients1))
#
# def summarize(idk):
#     a = 0
#     for i in idk:
#         print(i)
#         if type(i) == int or type(i) == float:
#             a = a + i
#         elif type(i) == tuple or type(i) == list:
#             a = a + summarize(i)
#         elif type(i) == str:
#             a += int(i)
#     return a
#
#
# heterogen_tuple = (25, 95, 78.1, 12, 13, 97, 36, 10, 12, 99, 38, 69, 73,
#                        (8,), 12, 60, 56, 28, 64, 36, 29, 51, 45, 24, 93, 22,
#                        0, 77, 83, 40, 59, 14, 29, 6, 66, 62, 38, 46, 98,
#                        62, 37, 81, [7], 79, 31, 34, 41, 37, 61, 71, 78, 21,
#                        2, 96, 99, 58, 24, 61, 99, '4', 27, 44, 94, 13,
#                        98, 72, 54, 0, 10, 61, 37, 57, 90, 88, 36, 71, 36,
#                        91, 63, 56, 34, 36, 14, 63, 79, 40, 43, 93, 88, 65,
#                        19, 0.5, 70, 37, 82, 14, 25, 38, 49, [1, 2, [5, 3]])
# #
# print(summarize(idk=heterogen_tuple))




# def triange():
#     a = int(input("Size: "))
#     b = input("Symbol: ")
#     i = 1
#     s = 1
#     if a % 2 != 0:
#         s += 1
#     while i != a // 2 + s:
#         print(b * i)
#         i += 1
#     if a % 2 != 0:
#         i -= 1
#     while i > 0:
#         i -= 1
#         print(b * i)
#
# triange()
#
# def arith_mean(*args):
#     a = 0
#     b = 0
#     for i in args:
#         a += i
#         b += 1
#     return a / b
#
# print(arith_mean(5, 5, 15, 25, 35))
#
# def func(string=input()):
#     num = []
#     letter = []
#     print(string)
#     for i in string:
#         if i.isdigit():
#             num.append(i)
#             string = string.replace(i, '')
#         elif i.isalpha():
#             letter.append(i)
#             string = string.replace(i, '')
#         else:
#             continue
#     print(*num)
#     print(*letter)
#     print(*string)
# func()

a = 20
print(int(list(str(a))[1]))