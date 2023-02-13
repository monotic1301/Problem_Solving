import sys

def bs(chi, num):
    s, e = 0, len(chi)-1
    res = 0
    while s <= e:
        mid = (s+e)//2
        if num <= chi[mid][1]:
            e = mid-1
            res = mid
        else:
            s = mid+1
    return res

n, m = map(int, sys.stdin.readline().split())

chi = []
cha = []
for _ in range(n):
    temp, num = sys.stdin.readline().split()
    chi.append([temp, int(num)])
for _ in range(m):
    cha= int(sys.stdin.readline())
    print(chi[bs(chi,cha)][0])

