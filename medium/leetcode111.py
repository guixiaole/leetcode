# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        就是最近简单的，按照每一层来计算。
        :param root:
        :return:
        """
        if not root:
            return 0
        queen = [(root, 1)]
        while len(queen) > 0:
            tree, pos = queen.pop()
            if tree.left is None and tree.right is None:
                return pos
            if tree.left is not None:
                queen.append((tree.left, pos + 1))
            if tree.right is not None:
                queen.append((tree.right, pos + 1))
