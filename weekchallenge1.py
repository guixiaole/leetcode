class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        dp = [0 for _ in range(n + 1)]
        pos = rounds[0]
        dp[rounds[0]] += 1
        for i in range(1, len(rounds)):
            #  此刻是在rounds[0]开始的
            if pos < rounds[i]:
                for j in range(pos + 1, rounds[i] + 1):
                    dp[j] += 1
            else:
                for j in range(pos + 1, n + 1):
                    dp[j] += 1
                for j in range(1, rounds[i] + 1):
                    dp[j] += 1
            pos = rounds[i]
        max_dp = []
        max_ = max(dp)
        for i in range(0, len(dp)):
            if dp[i] == max_:
                max_dp.append(i)
        return max_dp

    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        #  选的方式就是先选第一大的和第二大的。然后再选最小的。
        piles.sort(reverse=True)
        length = int(len(piles) // 3)
        my = 0
        for i in range(length):
            piles.pop(0)
            my += piles.pop(0)
            piles.pop(len(piles) - 1)
        return my

    def findLatestStep1(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        last_num = -1
        for i in range(len(arr) - 1, -1, -1):
            arr_copy = arr[:i + 1]
            arr_copy.sort()
            last = []
            last_dance = 1
            for j in range(1, len(arr_copy)):
                if arr_copy[j] - arr_copy[j - 1] > 1:
                    last.append(last_dance)
                    last_dance = 1
                else:
                    last_dance += 1
            last.append(last_dance)
            for h in range(len(last)):
                if last[h] == m:
                    last_num = i + 1
                    return last_num
        return last_num


if __name__ == '__main__':
    n = 4
    rounds = [1, 3, 1, 2]
    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    arr = [3, 5, 1, 2, 4]
    m = 2
    c = Solution()
    print(c.findLatestStep1(arr, m))
