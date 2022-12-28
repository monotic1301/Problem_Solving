import sys

moem = ['a','e','i','o','u']
while True:
    password = sys.stdin.readline().strip()
    if password == "end":
        break
    flag1 = 1
    flag2 = 0
    flag3 = 0
    count_m =0
    count_j = 0
    for i in range(len(password)):

        # print(count_m, count_j)
        if password[i] in moem:
            flag1 = 0
            count_m += 1
            count_j = 0
        else:
            count_m = 0
            count_j += 1
        if count_m >= 3 or count_j >= 3:
            flag2 = 1
            break
        if count_m >= 2 or count_j >=2:
            if password[i-1:i+1] == "ee" or password[i-1:i+1] =="oo":
                continue
            elif password[i] == password[i-1]:
                flag3 = 1
                break
    if flag1+flag2+flag3 == 0:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
