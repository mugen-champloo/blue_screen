# a_set = {[1, 2], [2, 3]}
#
#
# set_a = {1, 2, 3}
# set_b = frozenset({4, 5, 6})
# set_c = {set_b, 7, 8, 9}
# print(set_c)
# print(set("1, 2, 3, 4, 5, 6, 7"))

# set_a = set("123")
# print(set_a)

# set_a = set("22222")
# print(set_a)

# set_a = {1, 2, 3}
# set_b = {4, 5, 6}
# print(set_a+set_a)
# print(set_a*23)
#
# from sys import getsizeof
# number = 10050000
# my_list = list(range(number))
# my_tuple = tuple(range(number))
# my_set = set(range(number))
# my_list_size = getsizeof(my_list)
# my_tuple_size = getsizeof(my_tuple)
# my_set_size = getsizeof(my_set)
#
# print(f'Размер списка: {round(my_list_size / 1024 / 1024, 3)}  мб')
# print(f'размер кортежа: {round(my_tuple_size / 1024 / 1024, 3)}  мб')
# print(f' Размер множества {round(my_set_size / 1024 / 1024, 3)}  мб')

# my_set = set()
# print(type(my_set))
#
# my_set = {5,}
# print(type(my_set))

# set_a = {1, 2, 3, 4, 6, 7}
# set_b = {"а", "б", "в", "г"}
# set_c = {"Мастер и маргарита", 450, 1250, "переплет"}
# set_d = {2, 4, 5, (2, 9, 0)}

#
# set_c = {"Мастер и маргарита", 450, 1250, "переплет"}
# print(set(set_c.split()))

# set_c = {"Мастер и маргарита", 450, 1250, "переплет"}
# print(set(set_c))
#
# print(set(["красный", "синий", "зелееый"]))

# print(set({"артикул": 7889, "цвет": 989}))

# Так не работает
# print(set(123))
# А так работает
# print(set(str(12312)))
#
# st = {1, 2, 4, 2, 5, 6, 8, 9, 11}
# print(st)
# print(f'Количество элементов: {len(st)}, сумма элементов: {sum(st)}')
# print(f'Минимальное значение: {min(st)}, максимальное: {max(st)}')
#
# st = {"математика", "Физика", "Химия"}
# print("математика" in st)
# print("математика" not in st)
#
# st = {1, 2, 4, 2, 5, 6, 8, 9, 11}
# print(sorted(st))
# print(sorted(st, reverse=True))
#
# st = {1, 2, 4, 2, 5, 6, 8, 9, 11}
# sp = {1, 4, 3, 5, 7, 4, 11, 22, 23}
# print(sp != st)
# print(sp == st)
#
# st = {1, 2, 3} # подмножество
# sp = {1, 2, 3, 4} # надмножество
# print(sp > st)

# Это вообще не работает
# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st > sp)

# st = (1, 2, 3, 22, 0)
# set(st)
# print(st.pop())

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st.union(sp))
#
# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st | sp)

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st.intersection(sp))
#
# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st & sp)

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st ^ sp)
#

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st.update(sp))

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# st.intersection_update(sp)
# print(st)

# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st.difference_update(sp))
#
# st = {1, 2, 3, 22, 0}
# sp = {1, 45, 2, 6, 8}
# print(st.isdisjoint(sp))