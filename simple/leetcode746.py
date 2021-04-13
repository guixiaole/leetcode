from typing import List
import copy


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return min(cost[len(cost) - 1], cost[len(cost) - 2])


if __name__ == '__main__':
    c = Solution()
    cost = [10,15,20]
    print(c.minCostClimbingStairs(cost))

