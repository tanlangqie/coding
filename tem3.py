# -*- coding: utf-8 -*-#

# Name:   tem3.py
# Author: tangzhuang
# Date:   2021/7/11
# desc:         

dic = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
    'i': 105,
    'j': 106,
    'k': 107,
    'l': 108,
    'm': 109,
    'n': 110,
    'o': 111,
    'p': 112,
    'q': 113,
    'r': 114,
    's': 115,
    't': 116,
    'u': 117,
    'v': 118,
    'w': 119,
    'x': 120,
    'y': 121,
    'z': 122

}

A = list('xxcdefg')
B = list('cdefghi')
# print(A[0])
size = len(A)
tem = []
for i in range(size):
    d = abs(dic[A[i]] - dic[B[i]])
    tem.append(d)
print(tem)

res = []
for i in range(size):
    sum = 0
    t = 0
    for j in range(i,size):
        if sum+tem[j] <= 5:
            t += 1
            sum += tem[j]
        else:
            break
    res.append(t)

for i in range(size-1,size-2,-1):
    sum = 0
    t = 0
    for j in range(i,0,-1):
        if sum+tem[j] <= 5:
            t += 1
            sum += tem[j]
        else:
            break
    res[-1]=t

print(res)
print(max(res))


# for i in range(1,size):
#     if sum + tem[i] <= 5:
#         res.append(res[-1]+1)
#         sum += tem[i]
#     if tem[i-1] + tem[i]<=5:
#         res.append()
#     else:
#         res.append(0)
#
#
# print(tem)