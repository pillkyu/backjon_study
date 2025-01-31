import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            des_x, des_y = j, i


def bfs():
    visited = ground
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] != 0:
                visited[i][j] = -1
    queue = deque()
    time = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue.append((des_y, des_x, time))
    visited[des_y][des_x] = time
    while queue:
        y, x, time = queue.popleft()
        for i in range(4):
            ndx = x+dx[i]
            ndy = y+dy[i]
            if 0<=ndx<m and 0<=ndy<n:
                if visited[ndy][ndx] == -1:
                    visited[ndy][ndx] = time+1
                    queue.append((ndy, ndx, time+1))
    return visited

answer = bfs()
for row in answer:
    for col in row:
        print(col, end = ' ')
    print("")


