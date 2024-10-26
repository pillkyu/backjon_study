import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
dp[0] = A[0]
for i in range(1, N):
        dp[i] = A[i]
        point = 0
        for j in range(i):
            if A[i] > A[j] and point < dp[j]:
                point = dp[j]
        dp[i] += point



print(max(dp))

