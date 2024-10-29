import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
rank = [i for i in range(1,N+1)]

arr.sort()
answer = 0
for i in range(N):
    answer += abs(arr[i] - rank[i])
print(answer)