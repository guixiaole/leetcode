"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[[3],[20,9],[15,7]]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        使用栈去存储一层的数。然后再考虑是从左往右还是从右往左。
        应该设置两个栈

        TODO：这道题最简单的办法不应该就是把所有的顺序都遍历了，然后再奇数层倒回来就好了。
        这么简单的事怎么不能理解呢？

        :param root:
        :return:
        """

        res = []
        res_odd = []  # 设置了两个栈。进行切换。
        flag_ceng = 0
        if root is None:
            return res
        res.append([root, 0])
        res1 = [[root.val]]
        while len(res) >= 1 or len(res_odd) >= 1:
            if flag_ceng % 2 == 0:
                node, ceng = res.pop(-1)
                if len(res) <= 0:
                    flag_ceng += 1
            else:
                node, ceng = res_odd.pop(-1)
                if len(res_odd) <= 0:
                    flag_ceng += 1
            if (ceng + 1) % 2 == 0:
                if node.right is not None:
                    res.append([node.right, ceng + 1])
                if node.left is not None:
                    res.append([node.left, ceng + 1])


            else:

                if node.left is not None:
                    res_odd.append([node.left, ceng + 1])
                if node.right is not None:
                    res_odd.append([node.right, ceng + 1])

            if ceng != 0:
                if len(res1) <= ceng:
                    res1.append([node.val])
                else:
                    res1[ceng].append(node.val)
        return res1


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree1 = tree.left
    tree1.left = TreeNode(4)
    tree2 = tree.right
    # tree2.left = TreeNode(15)
    tree2.right = TreeNode(5)
    c = Solution()
    print(c.zigzagLevelOrder(tree))
