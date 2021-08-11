# # # -*- coding: utf-8 -*-#
# #
# # # Name:   tem2.py
# # # Author: tangzhuang
# # # Date:   2021/7/11
# # # desc:
# #
# # # -*- coding: utf-8 -*-#
# #
# # # Name:   tem1.py
# # # Author: tangzhuang
# # # Date:   2021/7/11
# # # desc:
# #
# import sys
#
# for line in sys.stdin:
#     n = map(int, line.split())
#     arr = map(int, line.split())
#
#     arr = sorted(arr)
#     size = len(arr)
#     for i in range(size - 2):
#         for j in range(i + 1, size - 1):
#             for k in range(j + 1, size):
#                 if arr[k] == arr[i] + 2 * arr[j]:
#                     print(arr[k], arr[i], arr[j])
#                 if arr[k] == arr[j] + 2 * arr[i]:
#                     print(arr[k], arr[j], arr[i])
#     print(0)
# arr = [2,7,3,0]
# arr = sorted(arr)
# size = len(arr)
# for i in range(size - 2):
#     for j in range(i+1, size - 1):
#         for k in range(j+1, size):
#             if arr[k] == arr[i] + 2 * arr[j]:
#                 print(arr[k], arr[i], arr[j])
#             if arr[k] == arr[j] + 2 * arr[i]:
#                 print(arr[k], arr[j], arr[i])
# print(0)


import sys

# for line in sys.stdin:
# n = sys.stdin.readline().strip()
# arr = map(int, sys.stdin.readline().strip().split())
# arr = [2, 7, 3, 0]
# arr = [7,7,0]
# arr = sorted(arr)
# size = len(arr)
# flag = 0
# for i in range(size - 2):
#     for j in range(i + 1, size - 1):
#         for k in range(j + 1, size):
#             # print(arr[i],arr[j],arr[k])
#             if arr[k] == arr[i] + 2 * arr[j]:
#                 print(arr[k], arr[i], arr[j])
#                 flag = 1
#
#             if arr[k] == arr[j] + 2 * arr[i]:
#                 print(arr[k], arr[j], arr[i])
#                 flag = 1
# if flag==0:
#     print(0)

arr = [0, 0, 0,0]
arr = sorted(arr)
size = len(arr)
flag = 0
# print(dp)
for i in range(size):
    for j in range(i+1,size):
        if arr[i] + 2 * arr[j] in arr[j+1:]:
            print(arr[i] + 2 * arr[j], arr[i], arr[j])
            flag = 1
        if arr[j] + 2 * arr[i] in arr[j+1:]:
            print(arr[j] + 2 * arr[i], arr[j], arr[i])
            flag = 1
if flag == 0:
    print(0)
