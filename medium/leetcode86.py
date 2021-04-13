# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 使用最笨的方法去做的话，就是将一个数组进行保存，使用双指针。
        left, right = 0, 0
        # 首先将数组保存数据
        res = []
        temp = head
        temp2= head
        while temp is not None:
            res.append(temp.val)
            temp = temp.next
        left_res,right_res = [], [x]
        for i in range(len(res)):
            if res[i]<x:
                left_res.append(res[i])
            elif res[i]>x:
                right_res.append(res[i])

        while temp2 is not  None:
            if left<len(left_res):
                temp2.val = left_res[left]
                left+=1
            else:
                temp2.val = right_res[right]
                right+=1
            temp2 = temp2.next


if __name__ == '__main__':
    node = ListNode(1)
    node1 = node
    node1.next = ListNode(4)
    node1 = node1.next
    node1.next = ListNode(3)
    node1 = node1.next
    node1.next = ListNode(2)
    node1 = node1.next
    node1.next = ListNode(5)
    node1 = node1.next
    node1.next = ListNode(2)
    x = 3
    c = Solution()
    print(c.partition(node,x))