"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        采用动态规划来做。每个动态规划里面存储最近的一个相似的
        :param s:
        :return:
        @gxl 8/19
        """
        dp = [-1 for _ in range(len(s))]
        dict = {}
        for i in range(len(s)):
            if dict.get(s[i]) is None:
                dp[i] = -1
                dict[s[i]] = i
            else:
                dp[i] = dict[s[i]]
                dict[s[i]] = i
        #  dp中存入的为所有最近的一个。开始循环dp
        if len(dict) == 1:
            count = 0
            for i in range(1, len(s) + 1):
                count = count + i
            return count

        count = len(s)  # 有一个初始值。
        for i in range(0, len(dp)):
            if dp[i] != -1:
                #  假设不等于-1的时候。那么久找到他最近的那个数字。

                flag_dp = dp[i]
                while flag_dp != -1:
                    right = i
                    left = flag_dp
                    while right > left:
                        if s[right] != s[left]:
                            break
                        else:
                            right -= 1
                            left += 1
                    if left >= right:
                        count += 1
                    flag_dp = dp[flag_dp]
        return count


if __name__ == '__main__':
    c = Solution()
    print(c.countSubstrings('abab'))
