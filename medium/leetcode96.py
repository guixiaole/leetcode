"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


def numTrees(n: int) -> int:
    dp = [0 for _ in range(n + 1)]

    dp[1] = 1
    if n == 1:
        return dp[1]
    dp[2] = 2
    if n == 2:
        return dp[2]
    dp[0] = 1
    for i in range(3, n + 1):
        for j in range(1, i + 1):
            # 分左边和右边，然后相乘
            left = j - 1
            right = i - j
            dp[i] += dp[left] * dp[right]
    return dp[n]


if __name__ == '__main__':
    print(numTrees(6))
