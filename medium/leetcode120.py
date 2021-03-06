from typing import List

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
'''


def minimumTotal(triangle: List[List[int]]) -> int:
    """
    先用双层dp试试，然后再想办法改成一层dp
    :param triangle:
    :return:
    #dp里面还有一个状态压缩的说法
    """
    dp = [[0 for p in range(len(triangle))] for h in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        j = i
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
    return min(dp[len(triangle) - 1])


def minimumTotal1(triangle: List[List[int]]) -> int:
    """
    :param triangle:
    :return:
    #dp里面还有一个状态压缩的说法
    由于dp
    """
    dp = [0 for i in range(len(triangle))]
    # 状态压缩
    dp[0] = triangle[0][0]
    for i in range(1, len(triangle)):
        dp[i] = dp[i - 1] + triangle[i][i]
        for j in range(i-1, 0, -1):
            dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        dp[0] += triangle[i][0]
    return min(dp)


if __name__ == '__main__':
    triangl = [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9],
               [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0],
               [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
               [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]]
    print(minimumTotal1(triangl))
