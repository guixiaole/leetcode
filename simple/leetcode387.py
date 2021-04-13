"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        使用hash表。
        :param s:
        :return:
        """
        table = {}
        for h in s:
            if h not in table.keys():
                table[h] = 1
            else:
                table[h] += 1
        for i in range(len(s)):
            if table[s[i]] == 1:
                return i
        return -1
