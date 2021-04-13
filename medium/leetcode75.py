from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  大概使用的是快排的思想。
        zero, one = 0, 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                temp = nums[zero]
                nums[zero] = nums[i]
                nums[i] = temp
                zero += 1
                one += 1
            elif nums[i] == 1:
                temp = nums[one]
                nums[one] = nums[i]
                nums[i] = temp
                one += 1
            i += 1
        if nums[len(nums) - 1] == 1:
            temp = nums[one]
            nums[one] = nums[len(nums) - 1]
            nums[len(nums) - 1] = temp
        elif nums[len(nums) - 1] == 0:
            temp = nums[zero]
            nums[zero] = nums[len(nums) - 1]
            nums[len(nums) - 1] = temp
        return nums


if __name__ == '__main__':
    c = Solution()
    print(c.sortColors([2,0,2,1,1,0]))
