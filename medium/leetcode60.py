class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        per = 1
        for i in range(1, n + 1):
            nums.append(i)
            per = per * i
        sum = ""
        while n > 0:
            if k % (per / n) == 0:
                temp = int(k / (per / n)) - 1
            else:
                temp = int(k / (per / n))
            sum += str(nums.pop(temp))
            per = int(per / n)
            k = k - (temp * per)
            n -= 1
        while len(nums) > 0:
            sum += str(nums.pop(0))
        return sum


if __name__ == '__main__':
    C = Solution()
    print(C.getPermutation(2, 2))
