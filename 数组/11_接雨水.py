# -*- coding: utf-8 -*-#

# Name:   11_接雨水.py
# Author: tangzhuang
# Date:   2024/4/2
# desc:         


"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
 

"""
#同时需要考虑数组的左右两侧----》双指针，
#能接的雨水容量呢肯定是个矩形，那接的水就是矩形的面积。矩形的长就是左右下标相减  矩形的高就是左右两个木板中短的哪个
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j,res = 0,len(height)-1,0
        while i < j:
            if height[i]<= height[j]:
                res = max(res,height[i]*(j-i))
                i += 1
            else:
                res = max(res,height[j]*(j-i))
                j-=1
        return res
