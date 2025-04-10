from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    movement = deque([[1,(0,0)]])
    while movement:
        a, d = movement.popleft()
        x = d[1]
        y = d[0]
        if x == m-1 and y == n-1:
            return a
        for dy,dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx = x + dx
            ny = y + dy
            if (0<=nx<m and 0<=ny<n):
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    movement.append([a+1,[ny,nx]])
    return -1

# def solution(maps):
#     answer = bfs(0,maps, [0,0])
    
#     return answer

# def dfs(move, maps, direction):
#     news = [(0,1),(1,0),(0,-1),(-1,0)]
#     n = len(maps)-1
#     m = len(maps[0])-1
#     y = direction[0] #행 row
#     x = direction[1] #열 col
    
#     if y==n and x == m:
#         return move + 1
#     flag = False
#     for go in news:
#         x += go[0]
#         y += go[1]
#         if 0<=x<m and 0<=y<=n and maps[x][y] != 0:
#             flag = True
#             maps[x][y] = 0
#             print(move)
#             bfs(move+1,maps, [x,y])
#     if flag == False:
#         return -1