import sys
N,K = map(int, sys.stdin.readline().split())
nation = list()
for n in range(N):
   na = list(map(int, sys.stdin.readline().split()))
   nation.append(na)

for i in range(len(nation)):
    if nation[i][0] == K:
        idx = i
        break

rank = 1
for i in range(len(nation)):
    if i == idx:
        continue
    if nation[i][1] > nation[idx][1]:
        rank += 1
    elif nation[i][1] == nation[idx][1] and nation[i][2] > nation[idx][2]:
        rank += 1
    elif nation[i][1] == nation[idx][1] and nation[i][2] == nation[idx][2] and nation[i][3] > nation[idx][3]:
        rank += 1
    else:
        continue

print(rank)