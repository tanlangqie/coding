# -*- coding: utf-8 -*-#

# Name:   518零钱兑换2.py
# Author: tangzhuang
# Date:   2021/7/18
# desc:         


### 递归  --》超时
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size = len(coins)
        path = []
        res = []

        def fun(coins,path,amount,res):
            if sum(path) > amount:    #剪枝
                return
            if sum(path) == amount:
                res.append(path)
                return
            for k,v in enumerate(coins):
                fun(coins[k:],path+[v],amount,res)     #剪枝
            return
        fun(coins,path,amount,res)

        return len(res)


#####  动态规划   #########

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

# 作者：carlsun-2
# 链接：https://leetcode-cn.com/problems/coin-change-2/solution/dai-ma-sui-xiang-lu-518-ling-qian-dui-hu-q7gm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。