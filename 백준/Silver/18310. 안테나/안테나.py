import sys

N = int(sys.stdin.readline())
house = list(map(int,sys.stdin.readline().split()))

house.sort()
s = N
idx = s//2
if s%2 == 0:
    print(house[idx-1])
else:
    print(house[idx])