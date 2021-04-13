"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。
示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A.sort()
        left, right = 0, 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                if i % 2 != 0:
                    left = i
                    break
        for i in range(len(A)):
            if A[i] % 2 == 1:
                if i % 2 != 1:
                    right = i
                    break
        while left <= len(A) and right <= len(A):
            if A[left] % 2 == 0:
                if left % 2 != 0:
                    temp = A[left]
                    A[left] = A[right]
                    A[right] = temp
                    left += 1
                    right += 1
                    flag = 0
                for i in range(left, len(A)):
                    if A[i] % 2 == 0:
                        if i % 2 != 0:
                            left = i
                            flag = 1
                            break
                if flag ==0:
                    break
                flag = 0
                for i in range(right, len(A)):
                    if A[i] % 2 == 1:
                        if i % 2 != 1:
                            right = i
                            flag = 1
                            break
                if flag ==0:
                    break
        return A
    """
    leetcode 1030
    给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
    另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
    返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，
    其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
    （你可以按任何满足此条件的顺序返回答案。）
    示例 1：
    输入：R = 1, C = 2, r0 = 0, c0 = 0
    输出：[[0,0],[0,1]]
    解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
    """
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        sort_cell = []
        for i in range(R):
            for j in range(C):
                distance = abs(i-r0)+abs(j-c0)
                sort_cell.append([distance,i,j])
        sort_cell.sort()
        for sort_cell_single in sort_cell:
            sort_cell_single.pop(0)
        return sort_cell


if __name__ == '__main__':
    A =[4,2,5,7]
    c = Solution()
    print(c.sortArrayByParityII(A))