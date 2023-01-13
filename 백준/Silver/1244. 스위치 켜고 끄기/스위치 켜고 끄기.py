import sys


N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().strip().split()))
switch = [bool(i) for i in switch]
stu = int(sys.stdin.readline())
for i in range(stu):
    se, num = map(int, sys.stdin.readline().strip().split())
    if se == 1:
        for m in range(N):
            if (m+1) % num == 0:
                switch[m] = not(switch[m])
    elif se == 2:
        temp = 0
        if len(switch)-num >= len(switch)//2:
            section = num-1
        else:
            section = len(switch)-num
        num -= 1
        for sec in range(1,section+1):
            if switch[num-sec] != switch[num+sec]:
                temp = sec-1
                break
            elif sec == section:
                temp = sec
        for j in range(num-temp,num+temp+1):
            switch[j] = not(switch[j])

for i in range(len(switch)):
    print(int(switch[i]),end="")
    if (i+1) % 20 == 0:
        print()
    else:
        if i == len(switch)-1:
            print("",end="")
        else:
            print(" ",end="")