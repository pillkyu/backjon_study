import sys
input = sys.stdin.readline

N,K = map(int, input().split())

bag = [list(map(int, input().split()))for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
#

for i in range(1, N+1):
    for j in range(1,K+1):
        if j>=bag[i-1][0]:
            dp[i][j] = max(bag[i-1][1]+ dp[i-1][j-bag[i-1][0]], dp[i-1][j])
            #탐색을 할 때 현재 배낭에 들어갈 수 있는 무게를 확인한 후 배낭 안에 들어갈 수 있는 최대값을 구하게 됨.
            #이 때 배낭의 남은 공간을 채울 수 있는 최댓값을 그 전 행에서 찾아서 가져오는 방식
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])



