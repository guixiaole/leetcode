"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:
2
"""
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 使用hash
        hashA_B = {}
        for i in A:
            for j in B:
                temp = i + j
                if str(temp) in hashA_B.keys():
                    hashA_B[str(temp)] += 1
                else:
                    hashA_B[str(temp)] += 1
        sum_zero = 0
        for h in C:
            for p in D:
                tempplus = h + p
                if str(-tempplus) in hashA_B.keys():
                    sum_zero += hashA_B[str(-tempplus)]
        return sum_zero
