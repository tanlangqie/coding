'''
0

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
方法一：动态规划
定义状态：dp[i] 表示以第 i 个数字为结尾的最长上升子序列的长度。即在 [0, ..., i] 的范围内，选择 以数字 nums[i] 结尾 
可以获得的最长上升子序列的长度。
注意：以第 i 个数字为结尾，即 要求 nums[i] 必须被选取。反正一个子序列一定会以一个数字结尾，那我就将状态这么定义，这一点是常见的。

状态转移方程：遍历到索引是 i 的数的时候，我们应该把索引是 [0, ... ,i - 1] 的 dp 都看一遍，
如果当前的数 nums[i] 严格大于之前的某个数，那么 nums[i] 就可以接在这个数后面形成一个更长的上升子序列。
把前面的 i 个数都看了，dp[i] 就是它们的最大值加 11。即比当前数要小的那些里头，找最大的，然后加 11 。

总结一下，状态转移方程是：

dp[i] = max{1 + dp[j] if j < i and nums[i] > nums[j]}
直接看下面的例子或者代码来理解这个状态转移方程。

最后不要忘记，扫描一遍这个 dp 数组，其中最大值的就是题目要求的最长上升子序列的长度。

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/two-sum/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



'''
class Solution:
    # 将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例
    # dp 的值： 1  1  1  2  2  3  4    4

    def lengthOfLIS(self, nums):
        size = len(nums)
        # 特判
        if size <= 1:
            return size

        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i], dp[j] + 1)
        # 最后要全部一看遍，取最大值
        return max(dp)

#
# 作者：liweiwei1419
# 链接：https: // leetcode - cn.com / problems / two - sum / solution / dong - tai - gui - hua - er - fen - cha - zhao - tan - xin - suan - fa - p /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。