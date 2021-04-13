from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        """
        思路是动态规划
        dp[j]=dp[start]+1
        :param clips:
        :param T:
        :return:
        """
        dp = [-1 for _ in range(T + 1)]
        dp[0] = 0
        for i in range(T + 1):
            for j in range(len(clips)):
                if clips[j][0] < i <= clips[j][1]:
                    if dp[i] != -1:
                        dp[i] = min(dp[clips[j][0]] + 1, dp[i])
                    else:
                        if dp[clips[j][0]]!=-1:
                            dp[i] = dp[clips[j][0]] + 1
        return dp[T]


if __name__ == '__main__':
    c = Solution()
    clip = clips = [[0,2],[4,8]]
    T = 5
    print(c.videoStitching(clip, T))
