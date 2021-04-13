from typing import List

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0

'''


def searchInsert(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def flowers(scores):
    # 首先找到最小的花朵。
    if len(scores) < 1:
        return 0
    min_s = 0
    for i in range(len(scores)):
        if scores[i] < scores[min_s]:
            min_s = i
    # 运用两个双向指针
    dp = [0 for _ in range(len(scores))]
    dp[min_s] = 1
    for i in range(min_s - 1, -1, -1):
        if scores[i] > scores[i + 1]:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = 1
    for i in range(min_s + 1, len(scores)):
        if scores[i] > scores[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    return sum(dp)


folwers_input = input()
f = list(map(int, folwers_input.split()))
print(flowers(f))
