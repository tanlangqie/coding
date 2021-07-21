# -*- coding: utf-8 -*-#

# Name:   二叉树子树问题.py
# Author: tangzhuang
# Date:   2021/7/9
# desc:  leetcode 572   一个树是另一个树的子树
"""

要判断一个树 t 是不是树 s 的子树，那么可以判断 t 是否和树 s 的任意子树相等。那么就转化成 100. Same Tree。
即，这个题的做法就是在 s 的每个子节点上，判断该子节点是否和 t 相等。

判断两个树是否相等的三个条件是与的关系，即：

当前两个树的根节点值相等；
并且，s 的左子树和 t 的左子树相等；
并且，s 的右子树和 t 的右子树相等。
而判断 t 是否为 s 的子树的三个条件是或的关系，即：

当前两棵树相等；
或者，t 是 s 的左子树；
或者，t 是 s 的右子树。
判断 是否是相等的树 与 是否

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/subtree-of-another-tree/solution/dui-cheng-mei-pan-duan-zi-shu-vs-pan-duan-xiang-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:  # 均为空   递归出口
            return True
        if not s or not t:  # 有一个非空
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:  # 递归出口
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

