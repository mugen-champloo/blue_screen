# def my_function(n):
#     return lambda a: a * n
# double = my_function(3)
# print(double(19))
#
# zt = "dafdacewfvcdvrhnhdgbvsrvawcerdcws"
# vowels = "aeyuoi"
# result = list(map(lambda x: "Гласная" if x in vowels else "согласная", zt))
# print(result)
#
num = [29,1,3,4,1,4,342,65,65,6,545,42,35,4,43,5,24,42,334,3,23,32,42,23,32,34,32,234,23,2,32,41,31,2,31,31,23,]
print(list(filter(lambda x: x > 6 and x % 2 == 0, num)))
def get_min_or_max(value='max'):
    return eval(f'lambda x: {value}(x)')
#
#
# lst = [3,2,4,21,5,6,7,4,8,7,33,4,24,5,6,32,4,5,3,4]
# max_func = get_min_or_max()
# min_func = get_min_or_max('min')
# print(max_func(lst))
# print(min_func(lst))

#  в отличии от обычных функий фнонимные не могут содержать return(), pass, assert, raise
#
# ops = [(lambda x, y: x +y), (lambda x, y: x / y), (lambda x, y: x * y), (lambda x, y: x - y)]
#
#
# x, y = int(input()), int(input())
# for i in range(len(ops)):
#     print(ops[i](x, y))

# ops = {'neg': lambda x: abs(x), 'pos': lambda x: x // 2, 'zero': lambda x: x + 5}
# lst = list(map(int, input().split()))
#
# for i in lst:
#     if i < 0:
#         print(ops['neg'](i))
#     if i > 0:
#         print(ops['pos'](i))
#     else:
#         print(ops['zero'](i))
#
# my_list = [3, 4, 5, 6, 7, 3, 1, 345, 5, 6, 6, ]
#
# cubes = map(lambda x: pow(x, 9), my_list)
# print(list(cubes))

# mt_list = [4, 5, 6, 7, 22, 34, 5, 4, 32, 4, 4, 32, 4, 32, 34, 3]
# print(list(filter(lambda x: x % 2 == 0, mt_list)))
#
# lst = ['roll', 'apple', 'book', 'circle', 'laptop']
#
# print(list(filter(lambda x: len(x) > 4, lst)))
# print(list(filter(lambda x: 'p' in x, lst)))
#
# print([i for i in lst if len(i) > 4])
# print([i for i in lst if "p" in lst])
#
# stack = []
#
# for i in range(1, 11):
#     stack.append(f"{i} элемент")
#     print(f"+ {i}-й элемент добавлен")
#     for i in stack:
#         print(i, end="")
# print('\n')
# for i in range(len(stack)):
#     print("В стеке: ", end="")
#     for i in stack:
#         print(i, end="")
#     print(f'\n{stack.pop()} удален из стека')
#
# from sys import getrecursionlimit
# from sys import setrecursionlimit
# print(getrecursionlimit()) # выводит лимит по умолчанию
# setrecursionlimit(2000) # Увеличивает лимит до 2000
# print(getrecursionlimit()) # Выводит новый лимит

# def greetings(st):
#     print(st)
#     if len(st) == 0:
#         return
#     else:
#         greetings(st[:-1])
#
# greetings("Hello world!")
#
# def greetings(st):
#     print(st)
#     if len(st) >\
#             0:
#         greetings(st[:-1])
#
# greetings("Hello world!")