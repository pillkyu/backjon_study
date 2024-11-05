import sys
from collections import deque

input = sys. stdin.readline
n,m,t = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
answer = None
answer_2 = None
queue.append((0,0,0))



def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    global answer, answer_2

    while queue:
        dist, x,y = queue.popleft()
        if x == m-1 and y == n-1:
            if answer is None or dist<answer:
                answer = dist
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if m>nx>=0 and n>ny>=0 and not visited[ny][nx] :
                if maze[ny][nx] == 0:
                    queue.append((dist+1, nx, ny))
                    visited[ny][nx] = True
                elif maze[ny][nx]== 2:
                    potential_dist = dist + 1 + (n - 1 - ny) + (m - 1 - nx)

                    if answer_2 is None or potential_dist<answer_2:
                        answer_2 = potential_dist
                    visited[ny][nx] = True
bfs()
# 최종 출력
if answer is not None and answer <= t:
    if answer_2 is not None:
        print(min(answer, answer_2))
    else:
        print(answer)

elif answer_2 is not None and answer_2 <= t:
    print(answer_2)
else:
    print('Fail')