# numbers = ([1, 2, 3, 4, 5], [6, 7, 8])
#
# numbers[1].extend([3, 5, 9])
# numbers[0].append([7, 7, 8])
# numbers[1][2] += 5
# print(numbers)
# print(numbers[0][5])
#
# from timeit import timeit
# times = 1000000
# t1 = timeit("list(['груша', 'виноград', 'яблоко', 'банан', 'апельсин0'])", number=times)
# t2 = timeit("list(['груша', 'виноград', 'яблоко', 'банан', 'апельсин0'])", number=times)
# diff = "{:.0%}".format((t2 - t1)/t1)
# print(f"Время копирования списка {times} раз: {t1}")
# print(f"Время копирования кортежа {times} раз: {t1}")
#
# print(diff)
#
# from sys import getsizeof
#
# numbers1 = ((1, 2, 3, 4,), (5, 4, 5))
# numbers2 = [[1, 2, 3, 4,], [5, 4, 5]]
# print(getsizeof(numbers1))
# print(getsizeof(numbers2))
#
# nums1 = (1, 2, 3)
# nums2 = (4, 5, 6)
# print(nums1 + nums2)
# print(nums1 * 3)

# t2 = ('груша', 'виноград', 'яблоко', 'банан', 'апельсин0')
# s1, s2, s3, s4, s5 = t2
# print(s1, s4)
#
# b = (2)
# print(type(b))
# a = (2,)
# print(type(a))
#
# lettsrs = 'a', 'b', 'c', 'd'
# print(lettsrs)
#
# num = [4, 6, 7]
# print(tuple(num))
# str = "Who are you"
# print(tuple(str))
# sett = {2, 3, 4, 5}
#
# print(tuple(sett))

#
# my_dict = {"fasdfdsa": 21, "dasfasd": 3212}
# print(tuple(my_dict))
#
# num = 312312312
# print(tuple(str((num))))
#
# st = "Я изучаю***Python"
# print((st.partition("***")))
#
# st = tuple(input().split())
# print(st)
#
#
# st = "I'm learning Python"
# sp = ["Python", "Maki", "Toji", "Fushiguro"]
# tuple1 = (*st,)
# tuple2 = (*sp,)
# print(tuple1)
# print(tuple2)
#
# sp = ["Python", "Maki", "Toji", "Fushiguro"]
# print(sp[0], sp[3])
# print(sp[1:])
# print(sp[::-1])
#
# sp = ["Python", "Maki", "Toji", "Fushiguro"]
# print(sp.index("Toji"))

# sp = ["Python", "Maki", "Toji", "Fushiguro"]
# print(len(sp))
# print(min(sp, key=len))
# print(max(sp, key=len))
# sd = (3, 4, 6, 12, 4)
# print(sum(sd))

#
# sd = (3, 4, 6, 12, 4)
# print(5 in sd)
#
# sp = ["Python", "Maki", "Toji", "Maki","Fushiguro"]
# print(sp.count("Maki"))

# sp = ["Python", "Maki", "Toji", "Maki","Fushiguro"]
# print(sorted(sp))
#
# sp = ["Python", "Maki", "Toji", "Maki","Fushiguro"]
# print(tuple(sorted(sp, reverse=True)))
#
# sp = ("F", "u", "s", "h", 'i', 'u', 'r', 'o')
# print("*".join(sp))
# #
# sp = ("Maki")
# print(list(sp))
#
# sp = (("Maki", 80), ("Toji", 90), ("Gojo", 100))
# print(dict(sp))
# #
# a = (1, 1, 4)
# a.clear()
# b = (1, 1, 5)
# print(a < b)
# print(a > b)

# heterogen_tuple = (25, 95, 78.1, 12, 13, 97, 36, 10, 12, 99, 38, 69, 73,
#                        (8,), 12, 60, 56, 28, 64, 36, 29, 51, 45, 24, 93, 22,
#                        0, 77, 83, 40, 59, 14, 29, 6, 66, 62, 38, 46, 98,
#                        62, 37, 81, [7], 79, 31, 34, 41, 37, 61, 71, 78, 21,
#                        2, 96, 99, 58, 24, 61, 99, '4', 27, 44, 94, 13,
#                        98, 72, 54, 0, 10, 61, 37, 57, 90, 88, 36, 71, 36,
#                        91, 63, 56, 34, 36, 14, 63, 79, 40, 43, 93, 88, 65,
#                        19, 0.5, 70, 37, 82, 14, 25, 38, 49)
#
# print(hm13.summarize(idk=heterogen_tuple))
from hm13 import username_generator
username_generator()