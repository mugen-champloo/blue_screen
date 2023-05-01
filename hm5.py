# students_info = {
#     'Alina Popova': {
#         'gpa': 4.5,
#         'is_allowed': True,
#         'subjects': ['math', 'history', 'biology', 'geometry', 'GE'],
#         'has_paid': True
#     },
#     'Nurlan Azimov': {
#         'gpa': 4.0,
#         'is_allowed': True,
#         'subjects': ['history', 'math', 'biology' 'GE', 'physics'],
#         'has_paid': False}
# }
# students_info["Alina naumova"] = students_info.pop("Alina Popova")
# print(students_info)
#
#
# students_info = {
#     'Alina Naumova': {
#         'gpa': 4.5,
#         'is_allowed': True,
#         'subjects': ['art', 'math', 'history', 'biology', 'geometry', 'GE'],
#         'has_paid': True
#     },
#     'Nurlan Azimov': {
#         'gpa': 4.0,
#         'is_allowed': True,
#         'subjects': ['history', 'math', 'biology', 'GE', 'physics', 'music'],
#         'has_paid': False
#     }}
#
# a = students_info["Nurlan Azimov"].pop("subjects")
# b = students_info["Alina Naumova"].pop("subjects")
# a = a + b
# a = set(a)
# a = list(a)
# a = sorted(a, key=str.lower)
# print(a)


# sad = {
#     "Students": {
#         1231: {
#             "Name": "Aziz",
#             "Age": 23,
#             "Courses": ["Front-End developing", "Back-End developing"],
#             "GPA": 3.6,
#             "Job": True
#             },
#         1235: {
#             "Name": "Nikita",
#             "Age": 26,
#             "Courses": ["UX-UI Design", "Back-End developing"],
#             "GPA": 2.1,
#             "Job": False
#             }
#         },
#     "Staff": {
#         "Mentors": {
#             "Name": "Alexandr",
#             "courses": ["Back-End developing"],
#             "ID": ([1211, "Alexandr007"]),
#             "Adress": ["Bishkek", "Chui", 81]
#         }
#     }
# }
#
# name = input("Введите ваше имя: ")
# figure = int(input("Введите количество сторон: "))
# ssss = {0: "Круг", 3: "Треугольник", 4: "Квадрат", 5: "Пятиугольник"}
# print(f"Здравствуй {name}  твоя фигура это: \n{ssss[figure]}")

# calls = input("Введите имя и номер контакта: ")
# who = input("Ну и чей номер тебе нужен? ")
# calls = "".join(calls)
# calls = calls.split(" ")
# a = calls.index(who)
# dct = {calls[a]: calls[a+1]}
# print(dct.get(calls[a]))


# year = {
#     1: "Январь",
#     2: "Февраль",
#     3: "Март",
#     4: "Апрель",
#     5: "Май",
#     6: "Июнь",
#     7: "Июль",
#     8: "Август",
#     9: "Сентябрь",
#     10: "Октябрь",
#     11: "Ноябрь",
#     12: "Декабрь"
# }
#
# a = int(input("Какой месяц тебе нужен? "))
# print(year.get(a, "Введите число от 1 до 12"))
#
# numbers = {'dict1': [11, 20, 30, 17, 6, 24, 90, 15, 17],
#            'dict2': [21, 33, 40, 10, 29, 31, 90, 12],
#            'dict3': [52, 34, 20, 21, 44, 22, 10, 87],
#            'dict4': [22, 54, 29, 21, 70, 88, 99, 34],
#            'dict5': [21, 40, 29, 21, 19, 32, 68, 77],
#            'dict6': [14, 60, 70, 10, 55, 61, 84, 99],
#            'dict7': [45, 80, 12, 23, 42, 22, 37, 90],
#            'dict8': [13, 14, 15, 26, 48, 92, 36, 11],
#            'dict9': [12, 70, 18, 28, 18, 28, 53, 91],
#            'dict10': [29, 79, 18, 28, 18, 28, 32, 55]}
#
# del numbers['dict1'][]
# print(numbers)

print(5%2)