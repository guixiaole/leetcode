"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


def addStrings(num1: str, num2: str) -> str:
    new_num = ""
    flag, i, j = 0, len(num2) - 1, len(num1) - 1
    while i >= 0 and j >= 0:
        int_num = int(num2[i]) + int(num1[j])
        if flag == 1:
            int_num += 1
            flag = 0
        if int_num >= 10:
            flag = 1
            int_num = int_num % 10
        new_num += str(int_num)
        i -= 1
        j -= 1
    if i == -1:
        while j >= 0:
            int_num = int(num1[j])
            if flag == 1:
                int_num += 1
                flag = 0
            if int_num >= 10:
                int_num = int_num % 10
                flag = 1
            new_num += str(int_num)
            j -= 1
        if flag == 1:
            new_num += str(1)

    else:
        while i >= 0:
            int_num = int(num2[i])
            if flag == 1:
                int_num += 1
                flag = 0
            if int_num >= 10:
                int_num = int_num % 10
                flag = 1
            new_num += str(int_num)
            i -= 1
        if flag == 1:
            new_num += str(1)
    num_return = ""
    for i in range(len(new_num) - 1, -1, -1):
        num_return += new_num[i]
    return num_return


if __name__ == '__main__':
    print(addStrings("1953", "1234"))
