# -*- coding: utf-8 -*-#

# Name:   tem.py
# Author: tangzhuang
# Date:   2021/7/17
# desc:         

# def fun(i, path,res):
#     if i == 3:
#         res.append(path)
#         return
#     # for k in range(i):
#     print("i=={},{}".format(i,id(path)))
#     fun(i+1, path+[i],res)
#     return
#
# path = []
# print(id(path))
# res = []
# fun(1, path,res)
# print(res)
# # print(id(path))
# # print(path)
# print(['a']+['b'])



res = []
path = []
i = 0
j = 0

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
def fun(triangle, i, j, path, res):
    if i == len(triangle):
        res.append(sum(path))
        return
    if i + 1 <= len(triangle) - 1:
        fun(triangle, i + 1, j, path + [triangle[i][j]], res)
    if i + 1 <= len(triangle) - 1 and j + 1 <= len(triangle[i + 1]) - 1:
        fun(triangle, i + 1, j + 1, path + [triangle[i][j]], res)
    return


fun(triangle, 0, 0, path, res)
print(min(res))