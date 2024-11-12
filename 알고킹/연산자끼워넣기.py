import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
max_num, min_num = -1000000000,1000000000
def dfs(plus, minus, multi, divide, cnt, result):
    global min_num, max_num
    if cnt == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
    else:
        if plus>0:
            dfs(plus-1, minus, multi, divide, cnt+1, result+A[cnt])
        if minus>0:
            dfs(plus, minus-1, multi, divide, cnt+1, result-A[cnt])
        if multi>0:
            dfs(plus, minus, multi-1, divide, cnt+1, result*A[cnt])
        if divide>0:
            if result<0:
                dfs(plus, minus, multi, divide-1, cnt+1, -(abs(result) // A[cnt]))
            else:
                dfs(plus, minus, multi, divide-1, cnt+1, result // A[cnt])
dfs(plus, minus, multi, divide, 1, A[0])
print(max_num)
print(min_num)