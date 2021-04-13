"""
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。
示例 1：
输入：s = "(abcd)"
输出："dcba"
示例 2：
输入：s = "(u(love)i)"
输出："iloveu"
示例 3：
输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：
输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        left, right = 0, len(s) - 1
        flag = left
        flag_pos = 1
        sr = ''
        sr1 = ['' for __ in range(len(s))]
        flag_s = [0 for _ in range(len(s))]
        while right >= left:
            print(s[flag])
            if s[flag] != '(' and s[flag] != ')':
                flag_s[flag] = 1
                sr += s[flag]
                flag += 1
                if flag_pos == 1:
                    left += 1
                else:
                    right -= 1
            else:
                if flag_pos == 1:
                    # 应该是寻找到相对应的括号。
                    flag = right
                    while s[flag] != ')':
                        flag -= 1
                        right -= 1
                        if right < left:
                            break
                    flag_s[flag] = 1
                    flag -= 1
                    right -= 1
                    flag_pos = 0
                    left += 1
                else:
                    flag = left
                    while s[flag] != '(':
                        pass
                    flag_pos = 1
                    right -= 1


if __name__ == '__main__':
    c = Solution()
    print(c.reverseParentheses("(u(love)i)"))
