class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        flag_len = 0
        for i in range(1, len(s)):
            if s[i] == s[0]:
                if s[i - 1] == s[len(s) - 1]:
                    if i+1<len(s) and s[i+1]==s[1]:
                        flag_len = i
                        break
                    else:
                        if len(s)<=2:
                            return True
        if flag_len == 0:
            return False
        flag = 0
        for i in range(i, len(s)):
            if s[flag] == s[i]:
                flag += 1
            else:
                return False
            if flag >=flag_len:
                flag = 0
        if flag != 0:
            return False
        else:
            return True
if __name__ == '__main__':
    C=Solution()
    print(C.repeatedSubstringPattern("abaababaab"))