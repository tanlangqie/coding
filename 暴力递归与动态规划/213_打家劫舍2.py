# -*- coding: utf-8 -*-#

# Name:   213_打家劫舍2.py
# Author: tangzhuang
# Date:   2024/3/9
# desc:         




# def rob( nums ) :
#     if len(nums)<=2:
#         return max(nums)
#     #第一种情况不选第一个元素,最后一个元素可以选
#     res_list1 = [0,nums[1]]
#     for i in range(2,len(nums)):
#         res_list1.append(max(max(res_list1[:i - 1]) + nums[i], res_list1[i - 1]))  #注意当考虑第i个位置的时候，有两种情况，
#                                     第一种是取第i-1个位置的最大值，另一种情况就是取 截止到i-2位置的最大值在加上第i个位置的值。 注意是截止第i-2而不是第i-2个位置。所以第二个max中用了 max(res_list1[:i-1])).中间可以连续多个值不取，所以是用的是截止，注意与第198题的区分。198题没有限制这一题有限制所以动态转移方程与之前不同
#                                         具体badcase如下例所示
#
#         # res_list1.append(max(res_list1[i-2]+nums[i],res_list1[i-1]))
#     res1 = max(res_list1)
#     print(res_list1)
#
#     #第二种情况选第一个元素，最后一个不可用选
#     res_list2 = [nums[0],0]
#     for i in range(2,len(nums)-1):
#         res_list2.append(max(max(res_list2[:i - 1]) + nums[i], res_list2[i - 1]))
#     res2 = max(res_list2)
#     print(res_list2)
#     return max(res1,res2)

# print(rob([4,1,2,7,5,3,1]))


# 20240331 出错  原因还是 [4,1,2,7,5,3,1] 这个case
def rob( nums) -> int:
    if len(nums) <= 2:
        return max(nums)
    dp = [0] * len(nums)
    # 第1种情况不要第1个元素，最后一个可以要
    dp[0] = 0
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    dd = [0] * len(nums)
    # 第2种情况要第1个元素,最后一个不能要
    dd[0] = nums[0]
    dd[1] = 0
    for i in range(2, len(nums) - 1):
        dd[i] = max(dd[i - 1], dd[i - 2] + nums[i])

    return max(dp[-1], dd[-2])
res = rob( [1,2,3,1])
print(res)