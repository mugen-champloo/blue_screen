# list1 = [1, 3, 5, 2, 5]
# list2 = [6, 7, 3, 1, 2]
# list3 = [i + j for i, j in zip(list1, list2)]
#
# for i in list1:
#     for j in list2:
#         print(i +j)
# print
#
# numbers = [1, 3, 5, 2, 5, 7, 3, 1, 2]
# my_dict = {n: numbers.count(n) for n in numbers}
# print(my_dict)
#
# numbers = "12 3 21 3 5 3 5 432 43 23 12 5 76 5 45 87 45 65 56 67 76"
# my_dict = {n: int(n) * 2 for n in numbers.split() if int(n) % 2 == 0}
# print(my_dict)
#
# my_dict = {'футболка': "товар", "размер": "XL", "цвет": "белый", "количество": 560}
# print('Yes' if "футболка" in my_dict else "нет в наличии")
#
# a = (i for i in range(5))
# print(a)

#
# a = (i for i in range(5))
# print(*a)
#
# a = tuple(i**2 for i in range(1, 19, 2))
# print(a)

# a = tuple(map(int, input().split()))
# c = (i for i in a if i > 0 )
# print(f'Tuple {c}, ')
# b = (i for i in a if i < 0 )
# print(b)
#
# a = tuple(input().strip().split())
# print(all(i == a[0] for i in a))
#
# print({i**2 for i in range(15)})
#
# print({ord(i) for i in input() if i.isalpha()})
#
# set_a = {i**2 if i % 2 == 0 else i **3 for i in (map(int, input().split()))}
# print(set_a)
#
# a = set(input())
# b = set(input())
# c = set(input())
# print("Yes" if a == b == c else "No")

