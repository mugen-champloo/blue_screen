# # import datetime
# # a = datetime.datetime.now()
# # day = lambda: a.day
# # month = lambda: a.month
# # year = lambda: a.year
# # print(f'День: {day()}\n'
# #       f'Месяц: {month()}\n'
# #       f'Год: {year()}')
# #
# # def fibonachi(n):
# #     a, b = 0, 1
# #     for i in range(n):
# #         print(a, " ", end="")
# #         a, b = b, a + b
# #
# #
# # fibonachi(int(input()))
# #
# # def function(a, b):
# #     x = []
# #     for i in a:
# #         for j in b:
# #             if i == j:
# #                 x.append(str(i))
# #                 break
# #             else:
# #                 continue
# #     x = " ".join(x)
# #     print("Пересечение: ", x)
# #
# # a1 = list(map(int, input().split()))
# # b1 = list(map(int, input().split()))
# #
# # function(a=a1, b=b1)
#
# def function(a, b):
#     x = ""
#     for i in a:
#         if sorted(list(i)) == sorted(list(b)):
#             x += i + " "
#         else:
#             continue
#     print(x)
#
#
# a1 = input().split()
# b1 = input()
# function(a=a1, b=b1)
# #каприз клоун колба колун крона уклон колыбель карта
