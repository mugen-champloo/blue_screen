# def midtown_nav(start, end):
#     a = 0
#     b = 0
#     strt = []
#     e = []
#     print(strt, e)
#     for i in start.split():
#         if not i.isalpha():
#             print(i)
#             strt.append(i)
#     return strt, e
# print(midtown_nav("8th Ave and W 38th St", "7th Ave and W 36th St"))
# lst = [2, 3, 5, 6, 74, 3, 2, 3, -2, 3, 4, 5, -2, 4, -6]
# print(lst.index(-6))

# def max_sum_between_two_negatives(arr):
#     ind = []
#     piece_of_shit = []
#     schetchik_indexa = 0
#     fininish = []
#     for i in arr:
#         if i < 0:
#             ind.append(schetchik_indexa)
#         schetchik_indexa += 1
#     if len(ind) <= 1 :
#         return -1
#     for i in range(len(ind)-1):
#         piece_of_shit.append(arr[ind[i]+1:ind[i+1]])
#     for i in piece_of_shit:
#         fininish.append(sum(i))
#     return max(fininish)


# def max_sum_between_two_negatives(arr):
#     i = 0
#     s = -1
#     while i < len(arr) and arr[i] >= 0:
#         i += 1
#     i += 1
#     while i < len(arr):
#         m = 0
#         while i < len(arr) and arr[i] >= 0:
#             m += arr[i]
#             i += 1
#         if i == len(arr):
#             return s
#         i += 1
#         if m > s:
#             s = m
#     return s
#
#
# print(max_sum_between_two_negatives(arr=[3, 2, -3, 1, 3, 52, 65 - 21, 21, 3 - 3, 1, 3, -1, 2, 5, -7]))


# print(sum([1, 5.2, 4, 0, -1]))
#
# a = 811181
# b = 0
# if len(str(a)) >= 6:
#
# lst = [10, 15, 20]
# for i in lst:
#     if i % 2:
#         lst.append(i)
#     print(lst)

