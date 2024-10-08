import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
work_list =[]
for _ in range(n):
    t,p = map(int, input().split())
    work_list.append((t,p))
for i in range(n):
    t,p = work_list[i]
    dp[i+1] = max(dp[i+1], dp[i])
    if i+t <=n:
        dp[i+t] = max(dp[i+t], dp[i]+p)
print(dp[0])

