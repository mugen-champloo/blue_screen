L = [{'name': 'Alex', 'age': 20}, {'name': 'Amanda', 'age': 30}, {'name': 'David', 'age': 15}]
print(sorted(L, key=lambda item: item['age']))


def rus_eng(rus, eng, letter):
    if letter in rus:
        print("rus")
    elif letter in eng:
        print("eng")
    else:
        print("symbol")

r = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
e = 'qwertyuiopasdfghjklzxcvbnm'
rus_eng(rus=r, eng=e, letter=input().lower())


def maskify(n):
    a = ''
    for i in range(len(n)-4):
        a += "#"
    return a + n[len(n)-4: len(n)]
print(maskify(input()))


def maxnum(n):
    a = 0
    for i in n:
        if i > a:
            a = i
        else:
            continue
    return a


print(max(map(int, input().split())))