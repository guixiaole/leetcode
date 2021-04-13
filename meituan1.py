n = int(input())
for i in range(n):
    user = input()
    if 'a' <= user[0] <= 'z' or 'A' <= user[0] <= 'Z':
        flag_num = False
        flag_error = True
        for j in range(len(user)):
            if 'a' <= user[j] <= 'z' or 'A' <= user[j] <= 'Z':
                pass
            elif '0' <= user[j] <= '9':
                flag_num = True
            else:
                flag_error = False
                break
        if flag_error and flag_num:
            print("Accept")
        else:
            print("Wrong")
    else:
        print("Wrong")
