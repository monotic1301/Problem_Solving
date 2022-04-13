N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
sum = 0
used = []
print(A)
for _ in range(len(A)):
    imax, idx = -1, 0
    print(used)
    for j in range(len(B)):
        if j in used:
            continue
        elif B[j] > imax:
            imax = B[j]
            idx = j
    used.append(idx)
print(used)
for i in range(N):
    sum += A[i] * B[used[i]]
print(sum)
