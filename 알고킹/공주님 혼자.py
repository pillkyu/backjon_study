import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
n,m,t = map(int, input().split())
maze = [list(map(int, input().split()))for _ in range(n)]
answer = None
answer_2 = None


queue.append((0,0,0))
def bfs():
    arr = [[False]*m for _ in range(n)]
    arr[0][0] = True
    global answer_2, answer
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        count,x,y = queue.popleft()
        if x== m-1 and y == n-1:
            if answer is None or answer>count:
                answer = count
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if m>nx>=0 and n>ny>=0 and not arr[ny][nx]:
                if maze[ny][nx] == 0:
                    queue.append((count+1,nx,ny))
                    arr[ny][nx] = True
                elif maze[ny][nx] == 2:
                    potential_count = count+1 + (m-nx-1)+ (n-ny-1)
                    if answer_2 is None or answer_2>potential_count:
                        answer_2 = potential_count
                    arr[ny][nx] = True
bfs()
if answer is not None and answer<=t:
    if answer_2 is not None:
        print(min(answer, answer_2))
    else:
        print(answer)
elif answer_2 is not None and answer_2 <= t:
    print(answer_2)
else:
    print('Fail')


