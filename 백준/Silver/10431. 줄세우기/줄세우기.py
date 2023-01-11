import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    students = list(map(int, sys.stdin.readline().strip().split()))
    n = students[0]
    students = students[1:]
    w = 0
    for i in range(len(students)):
        for j in range(i):
            if students[j] > students[i]:
                w += 1
    print(f'{n} {w}')
