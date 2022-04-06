#백준 18352 특정 도시의 거리 찾기 (실버2)
from collections import deque

N , M, K, X = map(int,input().split())
links = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    links[a].append(b)

visit = [-1] * (N+1)
visit[X] = 0
arrive = deque([X])

while arrive:
    a = arrive.popleft()
    for node in links[a]:
        if visit[node] == -1:
            visit[node] = visit[a] + 1
            arrive.append(node)

check = False
for i in range(1,N+1):
    if visit[i] == K:
        print(i)
        check = True
if not check:
    print(-1)