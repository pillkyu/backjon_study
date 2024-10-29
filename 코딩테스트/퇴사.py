import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    t, p = map(int, input().split())
    arr.append((t,p))

dp = [0]*(N+1)


for i in range(N):
    t,p = arr[i]
    dp[i+1] = max(dp[i+1], dp[i])
    if i+t <=N:
        dp[i+t] = max(dp[i+t], dp[i]+p)
print(dp[-1])