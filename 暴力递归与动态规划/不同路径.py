'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
深度优先遍历 栈   递归
'''

class Solution(object):
    def move(self,m, n):
        num = 0
        if (m == 1 & n == 1):
            return 1
        if (m > 1):
            num += self.move(m - 1, n)
        if (n > 1):
            num += self.move(m, n - 1)
        return num



s = Solution()
print(s.move(2,1))



'''
二维动态规划 --
class Solution(object):
        
    def uniquePaths(self, m, n):
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
    

#     def __init__(self):
#         self.count = 0
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         # count = 0
#         def helper(i,j,m,n):
#             if i == m - 1 and j == n -1:
#                 self.count += 1
#                 return
#             if i + 1 < m and j < n:
#                 helper(i+1,j,m,n)
#             if i < m and j + 1 < n:
#                 helper(i,j+1,m,n)
#         helper(0,0,m,n)
#         return self.count



# 作者：powcai
# 链接：https://leetcode-cn.com/problems/two-sum/solution/dong-tai-gui-hua-by-powcai-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





'''