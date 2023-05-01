# in_stock = {'груши', 'яблоки', 'бананы', 'апельсины', 'арбузы', 'киви', 'ананасы'}
# to_buy = {'киви', 'персики', 'бананы', 'яблоки', 'мандарины'}
# print(in_stock & to_buy)
# print((in_stock & to_buy) ^ to_buy)
#
# group = {'Andrew', 'Lola', 'Kate', 'Sara', 'Vincent', 'Jessie', 'Nate', 'Mia', 'Bob', 'Tom'}
# exam_succsess = {
#     "Tom": 4,
#     "Bill": 3,
#     "Mia": 5,
#     "Bob": 4,
#     "Kate": 4,
#     "Liam": 3,
#     "Sara": 5}
#
# a = set(exam_succsess.keys())
#
# print(sorted((group ^ a) & group))

# all_players = {'Jose', 'Noah', 'Harry', 'Luca', 'Jake', 'Henry', 'George', 'Theo', 'Oliver', 'Matthew', 'Aaron', 'Logan', 'Leo', 'Austin', 'Sebastian', 'Yusuf', 'Arthur', 'Oscar', 'Max'}
# directors_choice = {'Jose', 'Sebastian', 'Harry', 'Luca', 'Jake', 'Henry', 'George', 'Theo', 'Oliver', 'Matthew', 'Aaron'}
# coaches_choise = {'George', 'Theo', 'Oliver', 'Matthew', 'Aaron', 'Logan', 'Leo', 'Austin', 'Sebastian', 'Yusuf', 'Jake'}
# c = directors_choice & coaches_choise
# print(sorted(c))
# a = coaches_choise.union(directors_choice)
# print(sorted(a-c))
# print(sorted(all_players - a))

# a = int(input("Введите число от 420 до 540: "))
# print(f'Поставь будильник на {a // 60}:{a % 60}')
#
# n = int(input())
# print(f'Часов: {n // 3600}, Минут: {n % 3600 //60}, Секунды: {n % 3600 % 60}')

# a = "12341577392816704730470212"
# print(a.replace("1", "один"))

# a = list(map(int, input("Вводите числа: ").strip().split()))
# dct = dict()
# for i in a:
#     if i % 2 == 0:
#         dct[i] = "четное"
# print(dct)