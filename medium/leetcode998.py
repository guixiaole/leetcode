"""
最大树定义：一个树，其中每个节点的值都大于其子树中的任何其他值。
给出最大树的根节点 root。
就像之前的问题那样，给定的树是从表 A（root = Construct(A)）递归地使用下述 Construct(A) 例程构造的：
如果 A 为空，返回 null
否则，令 A[i] 作为 A 的最大元素。创建一个值为 A[i] 的根节点 root
root 的左子树将被构建为 Construct([A[0], A[1], ..., A[i-1]])
root 的右子树将被构建为 Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
返回 root
请注意，我们没有直接给定 A，只有一个根节点 root = Construct(A).
假设 B 是 A 的副本，并附加值 val。保证 B 中的值是不同的。
返回 Construct(B)。
示例 1
输入：root = [4,1,3,null,null,2], val = 5
输出：[5,4,null,1,3,null,null,2]
解释：A = [1,4,2,3], B = [1,4,2,3,5]
示例 2：
输入：root = [5,2,4,null,1], val = 3
输出：[5,2,4,null,1,null,3]
解释：A = [2,1,5,4], B = [2,1,5,4,3]
示例 3：
输入：root = [5,2,3,null,1], val = 4
输出：[5,2,4,null,1,3]
解释：A = [2,1,5,3], B = [2,1,5,3,4]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertIntoMaxTree(root: TreeNode, val: int) -> TreeNode:
    if val > root.val:
        q = TreeNode(val)
        q.left = root
        return q
    else:
        #  使用双指针
        nextq = root.right
        now = root
        while nextq is not None and val < nextq.val:
            now = nextq
            nextq = nextq.right

        now.right = TreeNode(val)
        if nextq is not None:
            now.right.left = nextq
    return root


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    """
    使用递归来构建最大的二叉树。
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return TreeNode(max(nums))
    max_num = nums.index(max(nums))
    root = TreeNode(max(nums))
    if max_num == 0:
        root.left = None
        root.right = constructMaximumBinaryTree(nums[max_num + 1:len(nums)])
    elif max_num == len(nums) - 1:
        root.right = None
        root.left = constructMaximumBinaryTree(nums[0:max_num])
    else:
        root.left = constructMaximumBinaryTree(nums[0:max_num])
        root.right = constructMaximumBinaryTree(nums[max_num + 1:len(nums)])
    return root


if __name__ == '__main__':
    root = constructMaximumBinaryTree([2, 1, 5, 4])
    insertIntoMaxTree(root, 3)
