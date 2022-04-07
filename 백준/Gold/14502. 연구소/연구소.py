from collections import deque
import copy

def bfs(n, m, lab_):
    visit_ = [[False for _ in range(m)] for _ in range(n)]
    count_ = 0
    q = deque([])
    for i_ in range(n):
        for j_ in range(m):
            if lab_[i_][j_] == 2 and visit_[i_][j_] is False:
                q.append((i_, j_))
                while q:
                    a, b = q.popleft()
                    visit_[a][b] = True
                    if a - 1 >= 0:
                        if lab_[a - 1][b] == 0:
                            lab_[a - 1][b] = 2
                            q.append((a - 1, b))
                    if a + 1 < n:
                        if lab_[a + 1][b] == 0:
                            lab_[a + 1][b] = 2
                            q.append((a + 1, b))
                    if b - 1 >= 0:
                        if lab_[a][b - 1] == 0:
                            lab_[a][b - 1] = 2
                            q.append((a, b - 1))
                    if b + 1 < m:
                        if lab_[a][b + 1] == 0:
                            lab_[a][b + 1] = 2
                            q.append((a, b + 1))
    for i__ in range(n):
        count_ += lab_[i__].count(0)
    return count_

N, M = map(int,input().split())

lab = []
for i in range(N):
    lab.append([int(i) for i in input().split()])

answer = 0
for i in range(N * M):
    for j in range(i + 1, N * M):
        for k in range(j + 1, N * M):
            if lab[i // M][i % M] == 0 and lab[j // M][j % M] == 0 and lab[k // M][k % M] == 0:
                lab[i // M][i % M] = 1
                lab[j // M][j % M] = 1
                lab[k // M][k % M] = 1
                lab_ = copy.deepcopy(lab)
                count = bfs(N, M, lab_)
                if answer < count:
                    answer = count
                lab[i // M][i % M] = 0
                lab[j // M][j % M] = 0
                lab[k // M][k % M] = 0
print(answer)