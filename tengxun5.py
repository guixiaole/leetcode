def countSubstrings(s):
    # aaababa #单数中心，双数中心 #aaaa
    # ababa #a,bab,ababa
    dp = [-1 for _ in range(len(s))]
    dict = {}
    for i in range(len(s)):
        if dict.get(s[i]) is None:
            dp[i] = -1
            dict[s[i]] = i
        else:
            dp[i] = dict[s[i]]
            dict[s[i]] = i
    if len(dict) == 1:
        return 1
    count = len(s)
    for i in range(0, len(dp)):
        if dp[i] != -1:
            flag_dp = dp[i]
            minus = 0
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
                    minus = right -left + 1
                flag_dp = dp[flag_dp]
            count -= minus
    return count

if __name__ == '__main__':
    s = input()
    n = int(input())
    for i in range(n):
        landr = input()
        landr1 = landr.strip().split()
        l, r = int(landr1[0]), int(landr1[1])
        s_copy = s[l - 1:r]
        count = countSubstrings(s_copy)
        print(count)
