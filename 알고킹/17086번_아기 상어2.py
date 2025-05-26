import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
count_map = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque()
answer = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            queue.append((i, j))
            count_map[i][j] = 0
while queue:
    y,x = queue.popleft()
    dx = [0, 0, -1, 1, 1, -1, -1, 1]
    dy = [1, -1, 0, 0, -1, -1, 1, 1]

    for i in range(8):
        ndx = x + dx[i]
        ndy = y + dy[i]
        if 0<=ndx<m and 0<=ndy<n:
            if map[ndy][ndx] == 0 and count_map[ndy][ndx] == -1:

                count_map[ndy][ndx] = count_map[y][x]+1
                queue.append((ndy, ndx))


for row in count_map:
    for one in row:
        answer = max(answer, one)
print(answer)

