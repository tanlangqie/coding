# -*- coding: utf-8 -*-#

# Name:   860柠檬水找零.py
# Author: tangzhuang
# Date:   2021/7/18
# desc:

"""


在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lemonade-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


"""

由于顾客只可能给你三个面值的钞票，而且我们一开始没有任何钞票，因此我们拥有的钞票面值只可能是 5 美元，10 美元和 2020 美元三种。基于此，我们可以进行如下的分类讨论。

5 美元，由于柠檬水的价格也为 5 美元，因此我们直接收下即可。

10 美元，我们需要找回 5 美元，如果没有 5 美元面值的钞票，则无法正确找零。

20 美元，我们需要找回 15 美元，此时有两种组合方式，一种是一张 10 美元和 5 美元的钞票，一种是 3 张 5 美元的钞票，如果两种组合方式都没有，则无法正确找零。当可以正确找零时，两种找零的方式中我们更倾向于第一种，即如果存在 55 美元和 1010 美元，我们就按第一种方式找零，否则按第二种方式找零，因为需要使用 55 美元的找零场景会比需要使用 1010 美元的找零场景多，我们需要尽可能保留 55 美元的钞票。

基于此，我们维护两个变量 \textit{five}five 和 \textit{ten}ten 表示当前手中拥有的 5 美元和 10 美元钞票的张数，从前往后遍历数组分类讨论即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/lemonade-change/solution/ning-meng-shui-zhao-ling-by-leetcode-sol-nvp7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

#理清思路，正常模拟过程即可
class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# 20240330 过
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=1
        c10=0
        c20=0
        if len(bills)<1:
            return None
        if bills[0]!=5:
            return False
        for i in bills[1:]:
            if i==5:
                c5 += 1
            if i==10:
                if c5>=1:
                    c5-=1
                    c10+=1
                else:
                    return False
            if i==20:
                if c5*5+c10*10>=15 and c5 >0:
                    if c10>=1:
                        c10-=1
                        c5-=1
                    else:
                        c5 -=3
                else:
                    return False
        return True