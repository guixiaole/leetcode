from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    res[i] += 1
        return res


if __name__ == '__main__':
    c = Solution()
    print(c.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
