from typing import List

"""
给定一个二叉树，返回它的 前序 遍历。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树的前序遍历，但是不能用递归。
        前序遍历：根->左->右
        :param root:
        :return:
        """
        queen = []
        res = [root.val]
        while root is not None:
            queen.append(root)
            res.append(root.val)
            root = root.left
        while queen is not None:
            root1 = queen.pop(0).right
            while root1 is not None:
                queen.append(root1)
                res.append(root1.val)
                root1 = root1.left
        return res








