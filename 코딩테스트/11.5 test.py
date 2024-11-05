import sys
from collections import deque

input = sys.stdin.readline
m,n,h = map(int, input().split())
box = [[list(map(int, input().split()))for _ in range(n)]for _ in range(h)]
queue = deque()
cant = False
answer = 0

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+ dx[i], y+ dy[i], z+dz[i]
            if 0<=nx<n and 0<= ny<m and 0<=nz<h:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y]+1
                    queue.append((nz,nx, ny))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i,j,k))
bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] ==0:
                cant = True
            else:
                answer = max(answer, box[i][j][k])
if cant:
    print(-1)
else:
    print(answer-1)