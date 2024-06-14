'''
0

编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：用三个指针，分别代表2 3 5已经遍历过的元素位置，开始时3个指针都在index=0处，结果中后面的数都由前面的数乘于2 3 5得到
每次取三个位置与对应2 3 5相乘的最小值
注意：多个条件之间用if，例如当最小值为6时，2的指针和3的指针都要后移
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n-1):
            res.append(min(res[idx2]*2,res[idx3]*3,res[idx5]*5))
            if res[-1] == res[idx2]*2:
                idx2 += 1
            if res[-1] == res[idx3]*3:
                print(res[-1])
                idx3 += 1
            if res[-1] == res[idx5]*5:
                idx5 += 1
        return res[-1]
# line.decode("utf8","ignore")
s = Solution()
res = s.nthUglyNumber(10)
print(res)