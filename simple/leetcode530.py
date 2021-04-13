# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        value = []


        def findvalue(self, root):
            if root is not None:
                value.append(root.val)
            if root.left is not None:
                findvalue(root.left.val)
            if root.right is not None:
                findvalue(root.right.val)
        findvalue(root)
        value.sort()
        minvalue = abs(value[1]-value[0])
        for i in range(1,len(value)):
            temp = abs(value[i]-value[i-1])
            if temp<minvalue:
                minvalue = temp
        return minvalue



