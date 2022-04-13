from collections import deque

N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
direction = [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],
             [(1,0),(0,1),(1,1)],
             [(1,0),(2,0),(2,1)],[(1,0),(2,0),(2,-1)],[(1,0),(1,1),(1,2)],
             [(1,0),(1,-1),(1,-2)],[(0,1),(1,1),(2,1)], [(0,1),(0,2),(1,2)],
             [(0,-1),(1,-1),(2,-1)],[(0,-1),(0,-2),(1,-2)],
             [(1,0),(1,-1),(2,0)],[(1,0),(1,-1),(1,1)],[(1,0),(2,0),(1,1)],[(0,-1),(0,1),(1,0)],
             [(0,1),(1,1),(1,2)],[(0,1),(1,0),(1,-1)],[(1,0),(1,-1),(2,-1)],[(1,0),(1,1),(2,1)]]
max_num = -1
for i in range(N):
    arr1 = []
    for j in range(M):
        for ds in direction:
            count = 0
            sum = arr[i][j]
            for i_,j_ in ds:
                count += 1
                if 0<= i+i_<N and 0<= j+j_<M:
                    sum += arr[i+i_][j+j_]
                else:
                    break
            if count ==3:
                arr1.append(sum)
    if max_num < max(arr1):
        max_num = max(arr1)
print(max_num)