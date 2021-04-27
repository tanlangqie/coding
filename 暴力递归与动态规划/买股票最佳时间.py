'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

解法：
动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
'''

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices)<2:
#             return 0
#         else:
#             minp, maxres = prices[0], 0
#             a = len(prices)
#             for i in range(1, a):
#                 minp = min(minp, prices[i])
#                 maxres = max(maxres, prices[i]-minp)
#             return maxres


'''
题目形式：有一个数组，求其中两个数x,y，满足x的索引小于y的索引，使得 x-y 最大。例如 arr = [3,7,2,6,4,1,9,8,5]， 最大回撤是6，对应的x=7,y=1。

题目难度：中等。

出现概率：约20%。这道题目可能以买卖股票的最佳时机，或者最大抬升等各种形式出现，这也是一道动态规划的史诗级范例。呦呵，又整上两重循环了，这循环写的很可以啊。


def max_drawdown(arr):
    assert len(arr)>2, "len(arr) should > 2!"
    x,y = arr[0:2]
    xmax = x
    maxdiff = x-y

    for i in range(2,len(arr)):
        if arr[i-1] > xmax:
            xmax = arr[i-1]
        if xmax - arr[i] > maxdiff:
            maxdiff = xmax - arr[i]
            x,y = xmax,arr[i]

    print("x=",x,",y=",y)
    return(maxdiff)
print(fun([3,7,2,6,4,1,9,8,5]))



def fun(prices):

    if len(prices)<2:
        return 0
    else:
        minp, maxv = 0,prices[0]
        a = len(prices)
        for i in range(1, a):
            maxv = max(maxv, prices[i])
            minp = min(minp, prices[i]-maxv)
    print(minp)




def fun(prices):

    if len(prices)<2:
        return 0
    else:
        minp, maxv = 0,prices[0]            #maxv代表最大值，minp代表最小的收益
        a = len(prices)
        for i in range(1, a):
            maxv = max(maxv, prices[i])
            minp = min(minp, prices[i]-maxv)
    print(minp)

print(fun([3,7,2,6,4,1,9,8,5]))


'''

import copy


#暴力递归------返回一个列表，在求列表的最值
# def fun(arr,count,i,path,res):
#     # print(id(path))
#     #count代表取了几只股票，如果已经取了两支了，则返回
#     if count == 2:
#         res.append(path)
#         return
#     if i == len(arr):
#         return
#     path = copy.deepcopy(path)
#     #不要第i个
#     fun(arr,count,i+1,path,res)
#
#     #要第i个
#     path.extend([arr[i]])
#     fun(arr,count+1,i+1,path,res)
#


#暴力递归 改进 --- 不需要列表，直接返回最值
def fun(arr,count,i,path,res):
    # print(id(path))
    if count == 2:
        return path[1] - path[0]
    if i == len(arr):
        return -100
    path = copy.deepcopy(path)
    #不要第i个
    a = fun(arr,count,i+1,path,res)

    #要第i个
    path.extend([arr[i]])
    b = fun(arr,count+1,i+1,path,res)
    return max(a,b)







arr = [2,1,5,7,3]
count = 0
path = []
i = 0
res = []
# fun(arr,count,i,path,res)
# print(res)


t = fun(arr,count,i,path,res)
print(t)

# def ab(i,p):
#     p.append(i)
#     if i == 2:
#         return
#     print(id(p))
#     print(p)
#     ab(i+1,p)
# ab(0,[1])