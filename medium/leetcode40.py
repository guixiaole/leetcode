from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []  # 结果列表
        tmp = []  # 可能组合

        def helpr(idx, total):
            if total == target:
                ans.append(tmp[::])
                return
            if total > target:
                return  # 如果大于，就结束。
            for i in range(idx, len(candidates)):
                if candidates[i - 1] == candidates[i] and i - 1 >= idx:
                    continue
                total += candidates[i]
                tmp.append(candidates[i])
                helpr(i + 1, total)
                tmp.pop()  # 假设不取的话
                total -= candidates[i]

        total = 0
        helpr(0, total)
        return ans


if __name__ == '__main__':
    c = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(c.combinationSum2(candidates, target))
