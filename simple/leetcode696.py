"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。
示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
请注意，一些重复出现的子串要计算它们出现的次数。
另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
"""


class Solution:
    def countBinarySubstrings1(self, s: str) -> int:

        count = 0
        for i in range(len(s) - 1):
            count_zero = 0
            count_one = 0
            flag = 1
            if s[i] == '0':
                count_zero += 1
            else:
                count_one += 1
            for j in range(i + 1, len(s)):
                if s[j] == s[j - 1]:
                    if s[j] == '0':
                        count_zero += 1
                    else:
                        count_one += 1
                else:
                    if flag == 1:
                        if s[j] == '0':
                            count_zero += 1
                        else:
                            count_one += 1
                        flag = 0
                    else:
                        break
                if count_one == count_zero:
                    count += 1
        return count

    def countBinarySubstrings(self, s: str) -> int:
        """
        首先进行分组。
        :param s:
        :return:
        """
        now, last = 1, 0
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                now += 1
            else:
                last = now
                now = 1
            if last >= now:
                count += 1
        return count


if __name__ == '__main__':
    c = Solution()
    print(c.countBinarySubstrings(
        "00110"))
