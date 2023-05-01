# codify = {'teachers': {'alex': {'experience': 4, 'is_teacher': True, 'stack': ['Python', 'Js', 'Java', ['Django', 'postgresql', 'Git']]}},
#           'support': {'amir': {'experience': 3, 'is_teacher': False, 'stack': ['Python', 'Js', 'Java', ['Django', 'postgresql', 'Git']]}},
#           'students': {'sani': ['17 years old', 'not stack', {'experince': 0, 'is_teacher': False, 'study': {'codify': False, 'makers': True}}]}}
# dct = codify.copy()
# codify["teachers"]["alex"]["experience"] = 6
# b = list(dct['teachers']['alex'].keys())
# s = b[-1]
# a = codify['teachers']['alex'].pop('stack')
# a[3].insert(3, "ООП")
# oop = {s: a}
# codify['teachers']['alex'].update(oop)
#
# codify["support"]["amir"]["is_teacher"] = True
# sup_keys = list(dct["support"]["amir"].keys())
# sup_keys1 = b[-1]
# sup_val = codify["support"]["amir"].pop('stack')
# sup_val.remove("Js")
# sup_val[2][1] = "DRF"
# js = {sup_keys1: sup_val}
# codify["support"]["amir"].update(js)
# #
# for_st = {"Hobby": "Coding"}
# # codify["students"]["sani"].update(for_st)
# codify["students"]["sani"][2]["study"]['codify'] = True
# codify["students"]["sani"][2]["study"]['makers'] = False
# codify["students"]["sani"].insert(1, for_st)
#
# print(codify)

#
# a = tuple(["Cairo", 21.7])
# population = (('Tokyo', 37.4), ('Delhi', 29.4), ('Shanghai', 26.3), ('Sao Paulo', 21.8), ('Mexico City', 21.7), a)
# print(population)


# #
# votes = {
#     'Will Smith': 'Miller',
#     'Andrew Tate': 'Trump',
#     'Elon Musk': 'Biden',
#     'Jeff Bezos': 'Trump',
#     'Chris Hemsworth': 'Trump',
#     'Mark Zuckerberg': 'Trump',
#     'Ye': 'Bush',
#     'Joe Rogan': 'Biden',
#     'MrBeast': 'Biden',
#     'Tim Urban': 'Biden',
#     'Vitalik Buterin': 'Biden',
#     'Keira Knightley': 'Biden',
#     'Magnus Carlsen': 'Biden',
#     'Theo Von': 'Miller'}
#
# a = list(votes.values())
# b = list(set(a))
# b.sort()
# print(b)
# print("Votes for Biden :", a.count(b[0]))
# print("Votes for Trump :", a.count(b[-1]))
# print("Votes for Bush :", a.count(b[1]))
# print("Votes for Miller :", a.count(b[2]))
#
# matrix = (
#     [1 ,2 ,3],
#     [],
#     [7, 8, 9]
# )
# a = list(matrix)
# a.pop(1)
# b = [4,['пять'],6]
# a.insert(1, b)
# # print(tuple(a))
a = int(input("Введите число: "))
b = str(a % 2)
match b:
    case "0":
        print("Четная")
    case "1":
        print("Нечетная")

#
# a = ("Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная",
#      "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная", "Нечетная", "Четная")
# b = int(input("Введите число: "))
# print(a[b])

#
# num = list(map(float, input("Введите числа: ").strip().split()))
# tuple(num)
# print("Максимальное число: ", max(num), "\nМинимальное число:", min(num), "\nСумма min и max :", sum(num))

# fruit = (["яблоки", 46], ["персики", 49], ["лимоны", 36], ["виноград", 190])
# fruit[-1][-1] = 75
# a = tuple([["айва", 42]])
# fruit = fruit + a
# print(fruit)

# info = (("Евгений Романов", 25, "+56(983)354-67-21"),
#         ("Марина Дятлова", 22, "+56(190)251-45-79"),
#         ("Кирилл Кудрявцев", 34, "+7(890)456-12-42"),
#         ("Сергей Дятлов", 24, "+56(190)156-42-99"),
#         ("Юлия Степанова", 21, "+16(398)355-33-09"),
#         ("Тимофей Иванов", 34, "+7(918)222-52-77"))
# info2 = tuple()
# n = int(0)
# print(info[n][-1][0:3])
# for i in info:
#     if info[n][-1][0:3] == "+56":
#         n += 1
#     elif info[n][-1][0:3] != "+56":
#         info2 = info2 + info[n]
#         n += 1
# print(info2)
