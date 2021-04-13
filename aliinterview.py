# n = int(input())
# while n:
#     all_lr = input()
#     temp = all_lr.strip().split()
#     l_int, r_int = int(temp[0]), int(temp[1])
#     count = 0
#     for i in range(l_int, r_int+1):
#         str_count = str(i)
#         len_count = len(str_count)
#         str_new = ''
#         while len_count > 1:
#             str_new = ''
#             flag = 0
#             while flag < len_count - 1:
#                 temp_shu = abs(int(str_count[flag]) - int(str_count[flag + 1]))
#                 str_new += str(temp_shu)
#                 flag += 1
#             str_count = str_new
#             len_count -= 1
#         if str_new == '':
#             str_new = str_count
#         if int(str_new) == 7:
#             count += 1
#     print(count)
#     n -= 1
