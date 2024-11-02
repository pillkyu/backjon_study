import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
m,n,h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
#여기까진 기본 세팅

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
cant_complete = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]== 0:
                cant_complete = True
            day = max(day, box[i][j][k])
if cant_complete:
    print(-1)
else:
    print(day -1)
#나중에 홀로 구현해봐야함. 답지고 보고 구현 후 이해만 함
