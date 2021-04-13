def factorial(n):
    # 请在下面编写代码
    # ********** Begin ********** #
    fac = 1
    if n >= 2:
        for i in range(2, n + 1):
            fac *= i
    if n < 0:
        fac = 'None'
    # ********** End ********** #
    # 请不要修改下面的代码
    return fac


if __name__ == '__main__':
    for num in [-5, 0, 10, 15, 20, 25, 30]:
        fac = factorial(num)
        print(fac)
    print('\n***********************\n')
