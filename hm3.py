# lst = list(range(0, 21, 2))
# print(lst)
# print(f"Самое бльшое число это {max(lst)}")
# print(f"Самое маленькое число это {min(lst)}")
# print(f"Сумма выших чисел равна  {sum(lst)}")
# print(f"ваш список {lst[::-1]}")

# lst = "The banana plant is the largest herbecous flowering plant. All the above-ground parts of a banana plant grow
# from a structure usually called a corm" lst = lst.split() print("Самое длинное слово ", max(lst, key=len)) lst2 =
# "<-->".join(lst) print(lst2)
#
# lst = [23, 5, 3, 2, 4, 67, 54, 2, 53]
# lst.
# lst.sort()
# print(lst)
# lst.reverse()
# del lst[0:2]
# lst.reverse()
# print(f"Ваш список с удаленными элементами {lst}")

# a = int(input("Введите число до 20: "))
# lst = range(0, a)
# print(f"Сумма чисел от 0 до {a} = {sum(lst)}")
#
# sur = input("Введите фамилии: ").title()
# sur = sur.split()
# sur.sort()
# print(sur)

# products = ['хлеб', "масло", "сыр"]
# lst = input("Введите наименование продуктов: ")
# lst = lst.split()
# lst.extend(products)
# print(lst)

#
# a = int(input("Введите номер: "))
# a.
# b = a//4+1
# print(b)

# lst = list(input("Введите предложение: "))
# a = int(lst.index("#"))
# del lst[a]
# z = "".join(lst)
# print(z)
# z = z.split(" ")
# print(max(z, key=len))
# Без труд#а не выловишь и рыбку из пруда

# lst = list(input("Введите предложение: "))
# del (lst[lst.index("#")])
# lst = "".join(lst)
# print(lst)
# lst = lst.split(" ")
# print(max(lst, key=len))

lst = input("Введите слово: ")
repeats = lst + "."[:-1]
lst = lst.replace("ббб", "бб")
lst = lst.replace("ппп", "пп")
lst = lst.replace("ффф", "фы")
lst = lst.replace("ккк", "кк")
lst = lst.replace("ссс", "сс")
lst = lst.replace("ттт", "тт")
lst = lst.replace("жжж", "жж")
lst = lst.replace("ллл", "лл")
lst = lst.replace("ммм", "мм")
lst = lst.replace("ннн", "нн")

lst1 = lst.find("бб")
lst2 = lst.find("пп")
lst3 = lst.find("фф")
lst4 = lst.find("кк")
lst5 = lst.find("сс")
lst6 = lst.find("тт")
lst7 = lst.find("жж")
lst8 = lst.find("лл")
lst9 = lst.find("мм")
lst10 = lst.find("нн")
ind = lst1+lst2+lst3+lst4+lst5+lst6+lst7+lst8+lst9+lst10+9
print("Исправленная буква '"+lst[ind]+"' количество повторов:", len(repeats)-len(lst))
print("Исправленное слово: ", lst)
