# -*- coding: utf-8 -*-#
#题目：规定1和A对应，2和B对应，3和C对应。那么一个字符串“111”可用转换为“AAA”或者“AK”与“KA”，找出所有的可能的转换数


# Name:   数字字符串转字母.py
# Author: tangzhuang
# Date:   2021/3/27
# desc:   要求出所有的转换结果--》’所有‘   ---》全部遍历----(从左到右)递归|动态规划。---》从左往右的全排列
           # 字符“1112235”从左往右 的第一步 可以有两种转换方式       转1位 '1'   转2位 “11”
           #第i个位置 是 0 则不可能转，如果是1则有两种可能性，如果是2则也有两种可能，如果是3~9只有一种可能


def num_to_str(string,index):
    """
    
    :param string: 数字字符串
    :param index: 
    :param res: 
    :return: 
    """
    res= 0
    #找到了一条可已转换的方法
    if index == len(string):
        return 1

    #i没有找到能转换的位置，此条路行不通，res不加1,返回0
    if string[index] == '0':
        return 0

    if string[index] == '1':
        #只转1个
        res += num_to_str(string, index+1)
        #一下转2个字符
        if index + 1 < len(string):
            res += num_to_str(string, index + 2)
    if string[index] == '2':
        #只转1个
        res += num_to_str(string, index+1)
        #一下转2个字符
        if (index + 1 < len(string)) and (string[index]>='0' and string[index]<='6'):
            res += num_to_str(string, index + 2)
    elif string[index] >= '3':
        res += num_to_str(string, index+1)
    return res

if __name__ == '__main__':


    string = '121'
    index = 0
    # all_pailie(string, index, res)
    res = num_to_str(string, index)

    print(res)