# -*- coding: utf-8 -*-#
#题目：n个皇后，在n*n的棋盘之上，任意两个皇后要不同行不同列，也不能同一个斜线。问有几种放置的方法

# Name:   n皇后问题.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:   二维数组上的所有遍历----递归。范围上的尝试模型



def n_queen(n,i,record):    #n代表总共有几个皇后  i代表当前遍历到第i个皇后
    if n == 1:
        return 0

    if i == n:
        return 1
    res = 0
    #对于每一列寻找合法的位置，往下搜索
    for j in range(n):
        if (is_val(record,i,j)):
            record[i] = j
            res += n_queen(n,i+1,record)

    return res



#判断第i个皇后放置在第i行的第j列会不会冲突
def is_val(record,i,j):
    """
    :param record: 列表，存放已经放置好的皇后位置。record[i]代表第i个皇后在第i行的位置
    :param i: 第i个皇后
    :param j: 第j个列
    :return: 
    """
    for k in range(i): #遍历之前的每一个皇后位置，判断第i个放置下来非法与否
        if (j==record[k]) or (abs(record[k]-j)==abs(i-k)):
            return False
    return True


if __name__ == "__main__":
    n = 6

    i = 0
    record = [0]*n   #记录那些列已经被放过
    res = n_queen(n, i, record)  # 第i个皇后开始放
    print(res)