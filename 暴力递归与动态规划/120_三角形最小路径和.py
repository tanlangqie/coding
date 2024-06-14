'''
0

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

注意，第i层的最大值不一定只是基于i-层，，，不是动态规划问题，有点像而已，此题需要遍历所有情况
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        # 建dp空间
        dp = [[0] * n for i in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):  #从第2行开始
            for k in range(i + 1):  #每行有i+1个元素
                if k == 0:
                    dp[i][k] = dp[i - 1][k] + triangle[i][k]
                elif k == i:
                    dp[i][k] = dp[i - 1][k - 1] + triangle[i][k]
                else:
                    dp[i][k] = min(dp[i - 1][k - 1], dp[i - 1][k]) + triangle[i][k]
        return min(dp[-1])

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/two-sum/solution/dong-tai-gui-hua-onkong-jian-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



#递归，时间超出限制
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = []
        path = []
        i = 0
        j = 0
        def fun(triangle,i,j,path,res):
            if i == len(triangle):
                res.append(sum(path))
                return

            fun(triangle,i+1,j,path+[triangle[i][j]],res)

            fun(triangle,i+1,j+1,path+[triangle[i][j]],res)
            return
        fun(triangle,0,0,path,res)
        return min(res)