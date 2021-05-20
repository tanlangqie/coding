'''
1

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

#思路与不同路径差不多，当前的最小值为 = min(左边最小值，上面最小值) + 当前位置的值，注意空间复杂度的优化

class Solution:
    #O(1)的复杂度，直接在原始的数组上修改
    def minPathSum(self, grid: List[List[int]]) -> int:
        # res = grid
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                    continue
                if j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                    continue
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


        #         #O(m*n)的复杂度，直接在原始的数组上修改

        #         res = grid
        #         m = len(grid)
        #         n = len(grid[0])
        #         for i in range(m):
        #             for j in range(n):
        #                 if i == 0 and j==0:
        #                     continue
        #                 if i == 0:
        #                     res[i][j] = res[i][j-1] + res[i][j]
        #                     continue
        #                 if j == 0:
        #                     res[i][j] = res[i-1][j] + res[i][j]
        #                     continue
        #                 res[i][j] = min(res[i-1][j],res[i][j-1]) + res[i][j]
        #         return res[-1][-1]


        # o(n)空间复杂度
        #         m = len(grid)
        #         n = len(grid[0])
        #         row = grid[0]
        #         for i in range(m):
        #             for j in range(n):
        #                 if i == 0 and j==0:
        #                     continue
        #                 if i == 0:
        #                     row[j] = row[j-1] + row[j]
        #                     continue
        #                 if j == 0:
        #                     row[j] += grid[i][j]
        #                     continue
        #                 row[j] = min(row[j],row[j-1]) + grid[i][j]

        #         return row[-1]