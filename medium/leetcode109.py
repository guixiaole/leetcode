"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        首先使用最平庸的解法去解决。用数组去存，然后将其再进行转换。
        假设不用数组的话，使用快慢指针也是一样的。慢指针走一步，快指针走两步。
        :param head:
        :return:
        """
        if head is None:
            return None
        listnode = []
        head1 = head
        while head1 is not None:
            listnode.append(head1.val)
            head1 = head1.next
        #  放入数组中之后，再开始组建二叉树
        node = self.creatTree(listnode)
        return node

    def creatTree(self, listnode):
        if len(listnode) <= 0:
            return
        half_len = int(len(listnode) // 2)
        node = TreeNode(listnode[half_len])
        # 应该有个边界
        if half_len - 1 >= 0:
            node.left = self.creatTree(listnode[0:half_len])
        if half_len + 1 < len(listnode):
            node.right = self.creatTree(listnode[half_len + 1:len(listnode) + 1])
        return node


if __name__ == '__main__':
    node = [-3, 0, 5, 9]
    Listnode = ListNode(10)
    list2 = Listnode
    for i in range(len(node)):
        list1 = ListNode(node[i])
        list2.next = list1
        list2 = list2.next
    c = Solution()
    c.sortedListToBST(Listnode)


