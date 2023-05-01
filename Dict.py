# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
#
# my_dict = dict(name = "Аркадий", age = "40", position = "PRO Drivft driver")
# print(my_dict)

# keys = ["color", "size", "count", "price"]
# values = ["blue", "65x67x89", 889, 1200]
# info = dict(zip(keys, values))
# print(info)
#
# new_dict = dict.fromkeys(["east", "west", "south", "north"], 0)
# print(new_dict)

# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict["color"], my_dict["price"])

# my_dict = {"color": "red", "color":"blue", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict)

# hr_info = {"сотрдники": {"имя": "Егор", "Должность": "пентестер"},
#            "сотрдник2": {"имя": "Егорка", "Должность": "DevOpsр"},
#            "сотрдник3": {"имя": "Елзавета", "Должность": "фронтэндер"}}
#
# print(hr_info["сотрдник2"]["Должность"]["имя"])

# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(len(my_dict))
#
# my_dict = {232: 352421412, 32111: 98080}
# print(sum(my_dict))
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(min(my_dict), max(my_dict))
# print(min(my_dict, key=len))
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# my_dict2 = {"asd": "reaad", "sssdaize": "XS", "griffit": "chert", "sprice": "650"}
# print({**my_dict, **my_dict2})
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# my_dict2 = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict == my_dict2)

# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())

#меняем словари
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# my_dict["color"] = "black"
# my_dict["bruh"] = "black"
# print(my_dict.get("color"))
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict["griffit"])

# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# print(my_dict.setdefault("color"))
#
# my_dict1 = {"color": "red", "size": "XS"}
# my_dict2 = {"color": "brown", "size": "X"}
# my_dict1.update(my_dict2)
# print(my_dict1)

# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# del my_dict["color"]
# print(my_dict)
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# s = my_dict.pop("color")
# print(s)
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# s = my_dict.popitem()
# print(s)
#
# my_dict = {"color": "red", "size": "XS", "Guts": "power", "price": "650"}
# new_dict = my_dict.copy()
# print(new_dict)