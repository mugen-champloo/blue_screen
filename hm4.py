# # lst = ['23', '23', '22', '12', '32', '23', '22', '25']
# # lst.remove("23")
#
# letters = 'йцукенгшщзхъфывапролджэячсмитьбюё'
# a = len(letters)
# b = list(letters)
# c = list(range(1, a+1))
# b.sort()
# ordered = dict(zip(b, c))
# print(f"Ordered = {ordered}")

# hr_info = {"сотрдники": {"имя": "Егор", "Должность": "пентестер"},
#            "сотрдник2": {"имя": "Егорка", "Должность": "DevOpsр"},
#            "сотрдник3": {"имя": "Елзавета", "Должность": "фронтэндер"}}
#
# name1 = input("Enter your name:").capitalize().split()
# name1 = "".join(name1)
# group1 = input("Enter your group: ").split()
# group1 = "".join(group1)
# sub1 = input("Enter your favorite subject: ").split()
#
# dct = {"name": name1, "group": group1, "subjects": sub1}
# print(dct)

# grades = {
#     'biology': 4,
#     'chemistry': 4,
#     'math': 3,
#     'GE': 5,
#     'physics': 4,
#     'history': 5
# }
# s = len(grades)
# a = sum(grades.values())/s
# print(round(a, 1))

# lst = ['23', '23', '22', '12', '32', '23', '22', '25']
# a = "  ".join(lst)
# a = a.replace("23", "Hello world", 3)
# print(a.split("  "))

# name = input("What's your name bastard? \n ")
# name = name.replace(" ", "")
# print("The length of your name is:", len(name))
# print("Your name is spelled:", list(name))

# n = int(input("Введите число n: "))
# x = input("Введите число x: ")
# s = (x + " ") * n
# print(list(map(int, s.strip().split())))

# products = input("Введите наименование продуктов: ").capitalize().split()
# price = input("Введите цену за продукты: ").split()
# dct = dict(zip(products, price))
# print(dct)
