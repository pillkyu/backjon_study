import sys
input = sys.stdin.readline
def find(x): #재귀적으로 부모노드를 찾는 함수
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b): #부모노드를 합쳐주는 함수
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root

N = int(input())
M = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
travel = list(map(int, input().split()))

parent = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if city[i][j] ==1:
            union(i,j)
root = find(travel[0]-1)
for i in travel[1:]:
    if find(i-1) != root:
        print("NO")
        break
else:
    print("YES")




