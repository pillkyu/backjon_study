import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())# x는 n, y는 m
tomato = [list(map(int, input().split())) for _ in range(m)]
def bfs():
    global tomato
    answer = 0
    queue = deque()
    for i in range(m):
        for j in range(n):
            if tomato[i][j] == 1:
                queue.append((i,j,0))

    while queue:
        y,x,count=queue.popleft()
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    queue.append((ny, nx, count+1))
        answer = count
    for row in tomato:
        for col in row:
            if col == 0:
                answer = -1

    print(answer)
bfs()


