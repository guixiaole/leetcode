"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        还是使用背包算法试试
        :param coins:
        :param amount:
        :return:
        """
        dp = [[amount + 1 for __ in range(amount + 1)] for _ in range(len(coins))]
        for h in range(len(coins)):
            dp[h][0] = 0
        for j in range(amount + 1):
            for i in range(len(coins)):
                if coins[i] <= j:
                    if j % coins[i] == 0:
                        dp[i][j] = j // coins[i]
                    dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i - 1][j], dp[i][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[len(coins) - 1][amount] == amount + 1:
            return -1
        return dp[len(coins) - 1][amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amoumt = 11
    c = Solution()
    print(c.coinChange(coins, amoumt))
