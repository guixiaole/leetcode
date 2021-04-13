"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left, right, flag = self.dfs(root)
        if abs(left - right) > 1 or flag == 0:
            return False
        else:
            return True

    def dfs(self, root):
        flag = 1
        if root.left is None and root.right is None:
            return 0, 0, 1
        else:
            if root.left is not None:
                left1, right1, flag1 = self.dfs(root.left)
                left = max(left1, right1) + 1
            else:
                left, flag1 = 0, 1
            if root.right is not None:
                left2, right2, flag2 = self.dfs(root.right)
                right = max(left2, right2) + 1
            else:
                right, flag2 = 0, 1
            if abs(left - right) > 1 or flag1 == 0 or flag2 == 0:
                flag = 0
            return left, right, flag
