# функция это мини программа внутри основной программы.
# Функция выполняется только тогда когда её вызывают
#
# def function():
#     print("Hello world")
# function()

# def my_funcrion(name):
#     print(f'Hello, {name}')
# my_funcrion("iroh")

# def function(name, lastname):
#     print(f'Hello, {name} {lastname}')
#
#
# function("Uncle", "Iroh")

# def function(name, lastname, occupation, age):
#     print(f'Worker #1 - {name} {lastname} {occupation} {age}')
#
# info1, info2, info3, info4 = 'Uncle', 'Iroh', 'tea-master', '64'
# function(info1, info2, info3, info4)
# function(info4, info3, info2, info1)

# def function(strt, build, ap, city="Moscow"):
#     print(f'Adres: c.{city}, st.{strt}, b.{build}, ap.{ap}')
#
# function("Ibragimova", 34, 12)
# function("Gorkogo", 12, 22, "bishkek")
#
# def sales(price, disc=5):
#     return price - price * disc / 100
#
#
# print(sales(5000))
# print(sales(5000, 10))
# print(sales(disc=15, price=5000))
#
# def function(*args):
#     print(f'min: {min(args)}, max {max(args)}')
#
#
# function(1, 2, 3, 4, 6, 2, 3, 1, 21, 32, 12, -3, -22, -20)
#
# def function(*args):
#     print(f'first word {args[0]} last word {args[-1]}')
#
#
# function('aple', 'lemon', 'orange', 'tomato')
#
#
# def function(*fruit):
#     print(f'first word {fruit[0]} last word {fruit[-1]}')
#
#
# function('aple', 'lemon', 'orange', 'tomato')


# def function(x, y, *args, ky=12, kx=13):
#     print(x, y, args, ky, kx)
#
# function(2, 5,3,6,7,8,5,4,8)
#
# def function(cat1, cat2, cat3):
#     print(f'youngest: {cat1}, eldest: {cat3}')
#
#
# function(cat1='tom', cat2='barsik', cat3='strela')

#
# def function(**kwargs):
#     print(f'The easiest metal: {min(kwargs, key=kwargs.get)} {min(kwargs.values())}, '
#           f'the heaviest metal {max(kwargs, key=kwargs.get)} {max(kwargs.values())}')
# function(osmii=22.3, cink=2.2, gold=3)
#
# def function(**country):
#     print(f'самая густо населенная страна - {max(country, key=country.get)} {max(country.values())},'
#           f'самая малонаселнная - {min(country, key=country.get)} {min(country.values())}')
#
# function(monako=122, moscow=3122, paris=222)
#
# def function(x, y, *args, ky=12, kx=13, **kwargs):
#     print(kwargs, x, y, args, ky, kx, )
#
#
# function(2, 5,3,6,7,8,5,4,8, sever=122, zapad=212, olololo=992)
# a = "@##$%^&*"
# print(a.isalpha())
#
# def my_function(stationery):
#     for i, j in enumerate(stationery):
#         print(f'Товар № {i + 1} - {j}')
#
#
# stuff = ["карандаш", "ручка", "блокнот", "альбом", "тетрадь"]
# my_function(stuff)

# def function():
#     pass
#
# def function(*args):
#     prod = 1
#     for i in args:
#         prod *= i
#     return prod
#
#
# print(function(3, 4, 5, 6, 8, 2, 4, 7))
#
# def calculations(a, b):
#     summa = a + b
#     diff = a - b
#     mul = a * b
#     div = a / b
#     return summa, diff, mul, div
#
#
# num1, num2 = int(input()), int(input())
#
# summa1, diff, mul, div = calculations(num1, num2)
# print(
#     f'Сумма : {summa1}\n'
#     f'Разность : {diff}\n'
#     f'Произведение : {mul}\n'
#     f'Результат деления : {diff:.2f}\n'
# )
#
# def bmi(h, w):
#     bmi = w / (h / 100) ** 2
#     if bmi <= 18.5:
#         return "У вас дефицит веса"
#     if bmi <= 24.9:
#         return "Вес в  норме"
#     if bmi <= 29.9:
#         return "Есть лишний вес"
#     else:
#         return "Срочно на диету"
#
# h = float(input("height: "))
# w = float(input("Weight: "))
# print(bmi(h, w))

#
# def bmi(h, w):
#     bmi = w / (h / 100) ** 2
#     if bmi <= 18.5:
#         res = "У вас дефицит веса"
#     elif bmi <= 24.9:
#         res = "Вес в  норме"
#     elif bmi <= 29.9:
#         res = "Есть лишний вес"
#     else:
#         res = "Срочно на диету"
#     return res
# h = float(input("height: "))
# w = float(input("Weight: "))
# print(bmi(h, w))
#
# def perfect_num(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum == n
#
#
# numbers = list(map(int, input().split()))
# flag = "no"
# for i in numbers:
#     if perfect_num(i):
#         flag = "yes"
#         break
# print(flag)
#
#
# def rus(n):
#     ed = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
#           'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
#           'девятнадцать']
#     des = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     res = ''
#     if n < 20:
#         res = ed[n-1]
#     elif n >= 20:
#         if int(list(str(n))[1]) == 0:
#             res = des[int(list(str(n))[0])-2]
#         else:
#             res = des[int(list(str(n))[0])-2] + " " + ed[int(list(str(n))[1])-1]
#     return res
#
# a = int(input())
# print(rus(a))

# def date(a):
#     b = int(a[1]) * int(a[4])
#     return b == int(a[-2:])
#
# ss = input()
# print(date(ss))

heterogen_tuple = (25, 95, 78.1, 12, 13, 97, 36, 10, 12, 99, 38, 69, 73,
    (8, 'word'), 12, 60, 56, 28, 64, 36, 29, 51, 45, 24, 93, 22,
    0, 77, 83, 40, 59, 14, 29, 6, 66, 62, 38, 46, 98,
    62, 37, 81, [None, 7], 79, 31, 34, 41, 37, 61, 71, 78, 21,
    2, 96, 99, 58, 24, 61, 99, '4', 27, 44, 94, 13,
    98, 72, 54, 0, 10, 61, 37, 57, 90, 88, 36, 71, 36,
    91, 63, 56, 34, 36, 14, 63, 79, 40, 43, 93, 88, 65,
    19, 0.5, 70, 37, 82, {14, (25, True)}, [[38], 1], 49, False, {'foo': 'bar'})


def summarizer(obj):
    total = 0
    for i in obj:
        if type(i) == int or type(i) == float:
            total = total + i
        elif type(i) == tuple or type(i) == list or type(i) == set:
            total = total + summarizer(i)
        elif type(i) == str:
            try:
                total += int(i)
            except ValueError:
                pass
        else:
            continue
    return total

print(summarizer(heterogen_tuple))