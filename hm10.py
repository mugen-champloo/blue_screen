# lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# a = [len(i) for i in lst]
# print(a)
#
# a = list(range(5, 60, 5))
# a.insert(a.index(20), 200)
# a.remove(20)
# print(sum(a))
# print(a)
# b = int(input("Enter a number from 1 till 60 : "))
# a.append(b)
# a = sorted(a)
# s = a.index(b)
# kk = b - a[s-1]
# kkk = a[s+1] - b
# if kk < kkk:
#     print(a[s-1])
# if kkk < kk:
#     print(a[s+1])
#
# else:
#     print("Something going wrong")

#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -43, -34, 3.44, 2.55,  "Lenovo", "Acer", "Asus"]
# B = [123, 43, 44, 8.16, -5, 3.26, 21, 22, -43, "Dell", "HP", "Lenovo", "Acer"]
# A.extend(B)
# s = list(i for i in A if type(i) == int)
# ss = list(i for i in A if type(i) == str)
# sss = list(i for i in A if type(i) == float)
# print(sorted(s))
# print(set(ss))
# print(sss)

# a = input().strip().split()
# b = set(a)
# print("Повтор" if len(a) > len(b) else "Принято")
