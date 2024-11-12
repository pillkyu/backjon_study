import sys
input = sys.stdin.readline
N = int(input())
parent_list = list(map(int, input().split()))
child_list  = [list() for _ in range(N)]
for child in range(1,N):
    call = parent_list[child]
    child_list[call].append(child)
def dfs(node):
    result =list()
    if not child_list[node]:
        return 0
    for i in child_list[node]:
        result.append(dfs(i))
    result.sort(reverse=True)
    result = [result[i]+i+1 for i in range(len(child_list[node]))]
    return max(result)
print(dfs(0))
