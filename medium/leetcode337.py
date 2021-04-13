"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，
我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
示例 1:
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob1(self, root: TreeNode) -> int:
        #  使用动态规划。首先把所有的树下的节点都开始收集起来。然后就开始用动态规划了。
        #  但是不知道树的根，就不能够用dp数组。
        if root is None:
            return 0
        dp = [0]
        stack = [(root, 1)]
        while len(stack) > 0:
            tree, length = stack.pop(0)
            if length >= len(dp):
                dp.append(tree.val)
            else:
                dp[length] += tree.val
            if tree.left is not None:
                stack.append((tree.left, length + 1))
            if tree.right is not None:
                stack.append((tree.right, length + 1))
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return max(dp[len(dp) - 1], dp[len(dp) - 2])

    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0
            left = _rob(root.left)
            right = _rob(root.right)
            v1 = root.val + left[1] + right[1]
            v2 = max(left) + max(right)
            return v1, v2
        return max(_rob(root))


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    left = root.left
    right = root.right
    left.right = TreeNode(4)
    a = Solution()
    print(a.rob(root))
