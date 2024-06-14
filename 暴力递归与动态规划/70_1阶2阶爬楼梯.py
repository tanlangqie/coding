#题目假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？注意：给定 n 是一个正整数。

# 原题：https://leetcode-cn.com/problems/climbing-stairs/

#递归  超出时间限制
class Solution:
    def climbStairs(self, n: int) -> int:
        def fun(n):
            if n <= 1:
                return n
            if n == 2:
                return 2
            return fun(n-1) + fun(n-2)
        return fun(n)



#动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return None

        if n == 1:
            return 1
        if n==2:
            return 2
        else:
            res = [0] * (n + 2)
            res[1] = 1
            res[2] = 2
            for i in range(3,n+1):
                res[i] = res[i-1] + res[i-2]
            return res
s = Solution()
print(s.climbStairs(4))