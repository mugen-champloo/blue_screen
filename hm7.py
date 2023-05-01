# animals = {
#     "homemade": {
#         "dog": {"Pipi": {"month": 4, "food": "anything", "is_friend": True}},
#         "cat": {"Barsik": {"month": 4, "food": "anything", "is_friend": False}},
#         "cow": {"Burenka": {"month": 4, "food": "anything", "is_friend": True}},
#     },
#     "fish": {
#         "1": [
#             "Norway redfish", "1kg",
#             ["this fish is very tasty", ["recommended by 70 percent of people"]],
#             "500som",
#             "22 fishes",
#         ],
#         "2": [
#             "Carp ",
#             "1kg",
#             ["this fish is not good", {"rating": 10}],
#             "1000som",
#             "30 fishes",
#         ],
#         "3": ["Walleye ", "1kg", "1000som", "30 fishes"],
#     },
#     "predator": [
#         [
#             "The tiger (Panthera tigris) is the largest living cat species and a member of the genus Panthera"
#         ],
#         [
#             "hello",
#             "world",
#             [
#                 "The",
#                 "wolf",
#                 "also",
#                 "known",
#                 "as",
#                 "the",
#                 "gray",
#                 "wolf",
#                 "or",
#                 "grey",
#                 "wolf,",
#                 "is",
#                 "a",
#                 "large",
#                 "canine",
#                 "native",
#                 "to",
#                 "Eurasia",
#                 "and",
#                 "North",
#                 "America",
#             ],
#         ],
#         [],
#     ],
# }
#
# animals["homemade"]["dog"]["Pipi"]["food"] = "Bones"
# animals["homemade"]["cat"]["Barsik"]["is_friend"] = True
# a = 'grass leaves'
# animals['homemade']['cow']['Burenka']["food"] = a.split()
#
# animals['fish']["1"].insert(1, "Norwegian perch lives about 15 years")
# del animals['fish']['3']
# b = {'3': ['for Walleye 1kg price is - 1000som']}
# animals['fish'].update(b)
# animals["fish"]['1'][3][1] = "".join(animals["fish"]['1'][3][1]).replace("70", "seventy")
# animals["fish"]['2'][2][1]['rating'] = 2
# print(animals)
#
# animals['predator'][0] = "".join(animals['predator'][0]).replace("e", "7")
# v = animals["predator"][1][2][::-1]
# animals["predator"][1][2] = " ".join(v)
# n = ['Hello world', 'Aegon Targarien']
# animals["predator"][-1].extend(n)
# print(animals)