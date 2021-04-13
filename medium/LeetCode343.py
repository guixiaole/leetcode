"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""


def integerBreak(n: int) -> int:
    """
    使用动态规划去做题。
    :param n:
    :return:
    """
    dp = [1 for _ in range(n + 1)]
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        dp[2], dp[3] = 2, 3
    for i in range(4, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j] * dp[i - j])
    return dp[n]
