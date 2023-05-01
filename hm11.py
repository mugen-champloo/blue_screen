# word = input("Write any word: ").lower()
# letter = input("Write any latter: ").lower()
# n = 0
# for i in word:
#     if letter == i:
#         n += 1
# if n == 0:
#     print(f'Your word {word} doesnt have any {letter}')
# else:
#     print(f'Your word {word} has {n} {letter}')

# start = int(input())
# end = int(input())
# sep = int(input())
# n = []
# for i in range(int(input()), int(input()), int(input())):
#     if i % 2 == 0:
#         continue
#     if i == 15 or i == 25 or i == 45:
#         print("Я больше не хочу работать!!!")
#         break
#     else:
#         n.append(i**2)
# print(n)

num = int(input())
for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')