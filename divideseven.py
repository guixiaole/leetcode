def divideseven(nums):
    length_seven = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            h = 0
            sum_all = 0
            flag = 1
            while h <= len(nums) - 1:
                if h == i:
                    h += 1
                else:
                    if j + 1 == h and flag == 1:
                        sum_all = sum_all * 10 + nums[i]
                        flag = 0
                    else:
                        sum_all = sum_all * 10 + nums[h]
                        h += 1
            if j == len(nums) - 1:
                sum_all = sum_all * 10 + nums[i]
            if sum_all % 7 == 0:
                length_seven += 1
    p, sum_all = 0, 0
    while p <= len(nums) - 1:
        sum_all = sum_all * 10 + nums[p]
        p += 1
    if sum_all % 7 == 0:
        length_seven += 1
    return length_seven


def divideseven1(nums):
    pass


if __name__ == '__main__':
    nums_seven = [1, 3, 2]
    print(divideseven(nums_seven))
