import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range (n)] for _ in range(h)]
queue = deque()
count = 0

def bfs():
    while queue:
        z,x,y = queue.popleft()

        dx = [0,0,1,-1,0,0]
        dy = [1,-1,0,0,0,0]
        dz = [0,0,0,0,1,-1]
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if n>nx>=0 and m>ny>=0 and h>nz>=0 :
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny]  =  box[z][x][y]+ 1
                    queue.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i,j,k))

bfs()
cant = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                cant = True
            count = max(count, box[i][j][k])
if cant:
    print(-1)
else:
    print(count-1)

