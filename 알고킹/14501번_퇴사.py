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
    dp[i+1] = max(dp[i+1], dp[i]) #현재까지의 최대 수익을 다음 날 전달
    if i+t <=n:#일을 할 수 있는 경우
        dp[i+t] = max(dp[i+t], dp[i]+p)
print(dp[n])
0 0 0 10 30 30 20 45 45 45
