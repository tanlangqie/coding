# -*- coding: utf-8 -*-#

# Name:   39组合总和.py
# Author: tangzhuang
# Date:   2021/7/17
# desc:   给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
"""

# 递归  + 剪枝
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        path = []
        def fun(candidates,target,res,path):
            if sum(path)>target:
                return
            if sum(path) == target:
                res.append(path)
                return
            for i,v in enumerate(candidates):
                fun(candidates[i:],target,res,path+[v])
            return
        fun(candidates,target,res,path)
        return res
