#그리디한 방식으로 탐색
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().split())

def BFS():
    queue = deque()
    count = 0
    visited = [0]*100001
    queue.append((n, count))

    while queue:
        cor, count = queue.popleft()

        if cor == k:
            return count
        if 0<=cor<100001 and visited[cor] == 0:
            queue.append((cor+1, count+1))
            queue.append((cor - 1, count + 1))
            queue.append((cor * 2, count + 1))
            visited[cor] = 1


print(BFS())


