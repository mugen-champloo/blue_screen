# sub = set(input("Enter your subject: ").lower().split())
# friends = {
#     "Piter Parker": {
#         "subjects": ["math", "biology", "history", "economics", "physics", "music"]
#     },
#     "Thor Odinson": {
#         "subjects": ["law", "physics", "math", "chemistry", "biology", "art"]
#     },
#     "Steve Rogers": {
#         "subjects": ["chemistry", "literature", "marketing", "math", "history"]
#     },
# }
# print("You will be with Piter in:", set(friends["Piter Parker"]["subjects"]).intersection(sub))
# print("You will be with Thor in:", set(friends["Thor Odinson"]["subjects"]).intersection(sub))
# print("You will be with Piter in:", set(friends["Steve Rogers"]["subjects"]).intersection(sub))
# a = set(friends["Steve Rogers"]["subjects"]).intersection(sub)
# b = set(friends["Thor Odinson"]["subjects"]).intersection(a)
# print("You wil be all together in:", set(friends["Piter Parker"]["subjects"]).intersection(b))
# #math chemistry history art coding
#
# a = input("Вводите текст: ")
# b = input("Букву: ").lower()
# print(a.count(b) + a.count(b.upper()))
#
# a = input("Введите текст: ")
# b = input("Введите букву которую нужно заменить: ")
# c = input("Введите букву на которую нужно заменить: ")
# d = a.replace(b.lower(), c)
# print(d.replace(b.upper(), c))
#
# treasury = {'house': {'room': {'door': ['table', ['gold coins diamonds jewelry'], 'closet']}}}
#
# treasure_chest = ['money', 'silver']
# spy_mission = treasury['house']['room']['door'].pop(1)
# spy_mission = " ".join(spy_mission)
# treasure_chest.extend(spy_mission.split())
# print(treasury)
# print(treasure_chest)

# name = input("Имя: ")
# surname = input("Фамилия: ")
# num = input("Номер: ")
# a = str(num[0].isdigit())
# b = {"True": "Новый образец", "False": "Старый номер"}
# print(f'{name}, {surname}, номерной знак {num}, у вас {b.get(a)}')