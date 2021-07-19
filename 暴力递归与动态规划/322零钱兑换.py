# -*- coding: utf-8 -*-#

# Name:   322零钱兑换.py
# Author: tangzhuang
# Date:   2021/7/18
# desc:   与39题组合总和一模一样


"""

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
"""



# 递归   +  剪纸  超出时间限制
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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

        if len(res)==0:
            return -1

        cnt = float('inf')
        for t in res:
            cnt = min(cnt,len(t))
        return cnt



## 方法2，记忆化搜索


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



### 动态规划   背包9解
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / coin - change / solution / 322 - ling - qian - dui - huan - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。