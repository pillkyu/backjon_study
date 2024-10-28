import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))

dp = [1] * N
for i in range(1,N):
    point = 0
    for j in range(i):
        if card[i]>card[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
#그냥 이 값보다 작은 값과 비교해서 뒷 값이 더 크면 그 카운트에 1을 추가해서 넣기
#너무 쉬운 문제
