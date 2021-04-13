s = input()
list_num = s.strip().split()
n = int(list_num[0])
final_select = int(list_num[1])
order = []
for i in range(n):
    num_order = input()
    num_order = num_order.strip().split()
    order.append((int(num_order[0]) + int(num_order[1]) * 2, n - i, int(num_order[0]), int(num_order[1])))
order.sort(reverse=True)
order_num = []
for i in range(0, final_select):
    order_num.append(n - order[i][1] + 1)
order_num.sort()
for j in range(0, len(order_num)):
    print(order_num[j], end=' ')
"""
8 4
5 10
8 9
1 4
7 9
6 10
9 45
3 48
1 49

[(26, 8, 9), (26, 6, 10), (25, 7, 9), (25, 5, 10), (9, 1, 4)]
[(25, 5, 10), (26, 8, 9), (9, 1, 4), (25, 7, 9), (26, 6, 10)]
"""
