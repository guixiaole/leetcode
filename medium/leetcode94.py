"""
给定一个二叉树，返回它的中序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        tree_list = []

        def inorder(tree):
            if tree.left is not None:
                inorder(tree.left)
            tree_list.append(tree.val)
            if tree.right is not None:
                inorder(tree.right)
        inorder(root)
        return tree_list


    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        不使用递归
        :param root:
        :return:
        """
        tree_tupe = []
        if root is None:
            return []
        tree_list = []
        while len(tree_list) > 0 or root is not None:
            while root is not None:
                tree_list.append(root)
                root = root.left
            root = tree_list.pop(-1)
            tree_tupe.append(root.val)
            root = root.right
        return tree_tupe
if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(4)
    tree1 = tree.left
    tree1.right = TreeNode(2)
    c=Solution()
    print(c.inorderTraversal1(tree))