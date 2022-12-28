import sys

N = int(sys.stdin.readline())
S = set()
for _ in range(N):
    c = sys.stdin.readline().split()
    if len(c) == 1:
        command = c[0]
    else:
        command = c[0]
        x = int(c[1])
    if command == "add":
        if x not in S:
            S.add(x)
    elif command == "remove":
        if x in S:
            S.remove(x)
    elif command == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command == "all":
        S = set(i for i in range(1,21))
    elif command == "empty":
        S = set()