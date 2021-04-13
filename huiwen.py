def huiwen(s):
    if judgehuiwen(s):
        return s
    #  如果不是回文串的话。
    dp = []
    for i in range(len(s) - 1):
        if s[i] == s[len(s) - 1]:
            dp.append(i)
    flag = len(s) - 1
    for i in range(0, len(dp)):
        left, right = dp[i], len(s) - 1
        while s[left] == s[right]:
            if right <= left:
                break
            left += 1
            right -= 1
        if right <= left:
            flag = dp[i]
            break
    length = flag-1
    for i in range(length, -1, -1):
        s += s[i]
    return s


def judgehuiwen(s):
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            break
    if i >= j:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "noo"
    print(huiwen(s))
