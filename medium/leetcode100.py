"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1:
输入:       1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
输出: true
示例 2:
输入:      1          1
          /           \
         2             2
        [1,2],     [1,null,2]
输出: false
示例 3:
输入:       1         1
          / \       / \
         2   1     1   2
        [1,2,1],   [1,1,2]
输出: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q is None and p is None:
            return True
        else:
            if q is None or p is None:
                return False
        statck_q = [(q, 1, "root")]
        statck_p = [(p, 1, "root")]
        flag = True
        while len(statck_q) > 0:
            q_tree, q_cengshu, q_pos = statck_q.pop(0)
            p_tree, p_cengshu, p_pos = statck_p.pop(0)
            if q_tree.val != p_tree.val or q_pos != p_pos or p_cengshu != q_cengshu:
                return False
            if q_tree.left is not None:
                statck_q.append((q_tree.left, q_cengshu + 1, "left"))
            if p_tree.left is not None:
                statck_p.append((p_tree.left, p_cengshu + 1, "left"))
            if q_tree.right is not None:
                statck_q.append((q_tree.right, q_cengshu + 1, "right"))
            if p_tree.right is not None:
                statck_p.append((p_tree.right, p_cengshu + 1, "right"))
        if len(statck_p) > 0:
            return False
        else:
            return True
