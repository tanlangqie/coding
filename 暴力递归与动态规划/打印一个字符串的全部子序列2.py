# -*- coding: utf-8 -*-#

# Name:         打印一个字符串的全部子序列.py
# Description:   用的列表
# Author:       tangzhuang
# Date:         2021/3/27
# desc:       字符串  abcd  他的子序列是 随机选择字符，保持相对位置就行  eg: ab  ac  acd

#思路 ： 出现了 ”全部“ 这种字眼，就代表要全部遍历-----》考虑递归与动态规划


def get_all_sub_str(string,index,path,res):
    """
    :param string: 输入的字符串，固定不变
    :param index: 遍历到的位置
    :param path: 记录每一个分支的路径（每一个子序列）
    :param res: 保存结果的列表
    :return: 
    """
    if index == len(string) :
        res.append(path)
        return

    #如果没选择index位置上的字符
    get_all_sub_str(string,index+1,path,res)

    #如果选择index位置上的字符
    get_all_sub_str(string,index+1,path+[string[index]],res)
    # return

if __name__ == '__main__':
    path= []
    res = []
    string = 'abc'
    index = 0
    get_all_sub_str(string, index, path, res)
    print(res)
    # a = ''
    # b = 'a'
    # c =a+b+'d'
    # print(c)