# Definition for a binary tree node.
"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    #  利用dfs，将所有的都入栈，然后并且标记好层数也入栈
    if root is None:
        return 0
    statck = [(root, 1)]
    max_len = 1
    while len(statck) >= 1:
        #  然后开始慢慢出栈
        tree, lentree = statck.pop(0)
        if tree.right is not None:
            statck.append((tree.right, lentree + 1))
        if tree.left is not None:
            statck.append((tree.left, lentree + 1))
        if lentree > max_len:
            max_len = lentree
    return max_len
