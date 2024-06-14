# -*- coding: utf-8 -*-#

# Name:   平衡二叉树.py
# Author: tangzhuang
# Date:   2021/7/8
# desc:  https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/

# 一棵二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树（左右子树高度相差1以内）。或者树为空

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

