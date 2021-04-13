"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode, k: int) -> int:
    #  利用中序输出
    tree = root
    statck = []
    while tree is not None or len(statck) > 0:
        while tree is not None:
            statck.append(tree)
            tree = tree.left
        tree = statck.pop(len(statck) - 1)  # 取出栈顶元素
        if k == 1:
            return tree.val
        else:
            k -= 1
        tree = tree.right


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(4)
    tree1 = tree.left
    tree1.right = TreeNode(2)
    print(kthSmallest(tree, 1))
