import sys
input= sys.stdin.readline
from collections import deque
T = int(input())

def bfs():
    global cabbage, ground, bug
    while cabbage:
        y, x=cabbage.popleft()

        if ground[y][x] == 1:
            bug += 1
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]

            meta = deque()
            meta.append((y,x))
            ground[y][x] = 0
            while meta:
                y, x = meta.popleft()
                for i in range(4):
                    xdx = dx[i]+x
                    ydy = dy[i]+y
                    if 0 <= xdx < m and 0 <= ydy < n:

                        if ground[ydy][xdx] == 1:
                            ground[ydy][xdx] = 0
                            meta.append((ydy, xdx))



for _ in range(T):
    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    cabbage = deque()
    bug = 0
    for _ in range(k):
        x, y = map(int,input().split())
        ground[y][x] = 1
        cabbage.append((y,x))
    bfs()
    print(bug)


