"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
IndentationError: unindent does not match any outer indentation level
                         ^
    res = self.dfs(digits)
Line 8  (Solution.py)
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        思路是使用深度搜索
        :param digits:
        :return:
        """

        res = self.dfs(digits)
        return res
    def dfs(self, s: str):
        dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        select = dict[s[0]]
        for i in range(len(select)):
            if len(s) > 1:
                temp = self.dfs(s[1:])
                for j in range(len(temp)):
                    res.append(select[i] + temp[j])
            else:
                return select
        return res


if __name__ == '__main__':
    C = Solution()
    print(C.letterCombinations('2344'))
