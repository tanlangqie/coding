# -*- coding: utf-8 -*-#

# Name:    字符串的全排列.py
# Author:  tangzhuang
# Date:    2021/3/27
# desc:    字符串“abc”的全排列--》‘abc’,'bca','cab','acb'等等
#思路： 全排列---》全---》全部遍历----(从左到右)递归|动态规划......   每个字符长是3，也就是需要走3步，每一步都有多种可能，eg:第一个位置上
#可能是 a或者b或者c

def change_str(string,i,j):
    """
    :param string: 字符串
    :param i: 字符索引
    :param j: 字符索引
    :return: 返回交换位置后的字符串
    """
    str1 = list(string)
    str1[i],str1[j] = str1[j],str1[i]
    return ''.join(str1)


#求一个字符串的全部排列,可能会有重复---eg:aaa 的全排列全是aaa
def all_pailie(string,index,res):
    """
    
    :param string: 每次要参与排序的字符串，每次会变
    :param index: 每次的位置
    :param res: 最终结果
    :return: 
    """

    if index == len(string):
        res.append(string)
        return
    #对于每一个index，从他本身开始，依次和后面每一个位置的字符交换位置
    for j in range(index,len(string)):
        new_str = change_str(string, index, j)
        all_pailie(new_str, index + 1, res)
        # change_str(string, index, j)


# 求一个字符串的全部排列,可能不要重复---分支限界法
def all_pailie2(string, index, res):
    """

    :param string: 每次要参与排序的字符串，每次会变
    :param index: 每次的位置
    :param res: 最终结果
    :return: 
    """

    if index == len(string):
        res.append(string)
        return

    #分支限界法，记录每个字符是否出现过  【‘a','b',---'z'】
    visit = [0] * 26

    # 对于每一个index，从他本身开始，依次和后面每一个位置的字符交换位置
    for j in range(index, len(string)):
        #如果该字符没出现过，那么才进行后续交换
        if visit[ord(string[j])-ord('a')]==0:
            visit[ord(string[j])-ord('a')] = 1
            new_str = change_str(string, index, j)
            all_pailie2(new_str, index + 1, res)


if __name__ == '__main__':
    path= ''
    res = []
    string = 'aaa'
    index = 0
    # all_pailie(string, index, res)
    all_pailie2(string, index, res)

    print(res)






# ord('a') 求字符的阿斯科马值，可用来进行字符间的加减计算