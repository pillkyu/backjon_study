import sys
from collections import deque
input = sys.stdin.readline
# N, M = map(int, input().split())
# node = [[] for _ in range(N+1)]
# count = 0
# visited = [0] * (N + 1)
# visited[0] = 1
#
# for _ in range(M):
#     u, v = map(int, input().split())
#     node[u].append(v)
#     node[v].append(u)
# def Bfs(n):
#     global count, visited
#     visited[n] = 1
#     queue = deque()
#     for nod in node[n]:
#         queue.append(nod)
#     while queue:
#         visit = queue.popleft()
#         if visited[visit] == 0:
#             visited[visit] = 1
#             for nod in node[visit]:
#                 queue.append(nod)
#     count += 1
#     if 0 in visited:
#         Bfs(visited.index(0))
# Bfs(1)
# print(count)
def find(x):
    if parent[x] !=  x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
v,e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
for i in range(e):
    a, b = map(int, input().split())
    union(a,b)
roots = set()
for i in range(1, v+1):
    roots.add(find(i))

print(len(roots))



