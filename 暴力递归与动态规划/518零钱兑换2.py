# -*- coding: utf-8 -*-#

# Name:   518零钱兑换2.py
# Author: tangzhuang
# Date:   2021/7/18
# desc:   与322的零钱兑换是同一个题，只是题目要的输出结果不一致
"""

给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。 

题目数据保证结果符合 32 位带符号整数。

"""


### 递归  --》超时

class Solution:
    def coinChange(self, coins , amount  ) -> int:
        path = []
        res = []

        def fun(coins,index,path,amount,res):
            print(coins,index,path,amount,res)
            if sum(path) > amount:    #剪枝
                return
            if sum(path) == amount:
                res.append(path)
                return
            if index>=len(coins):
                return
            for i in range(amount//coins[index]+1):   #剪枝
                if sum(path)+coins[index]<=amount:
                    fun(coins,index+1,path[:]+[coins[index]]*i,amount,res)
            # fun(coins, index+1, path, amount, res)
            return
        fun(coins,0,path,amount,res)

        return len(res)
s = Solution()
pp = s.coinChange([1, 2, 5],5)
print(pp)


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