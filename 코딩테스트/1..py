#징검다리 건너기
import sys
input = sys.stdin.readline
N = int(input())
stone = list(map(int, input().split()))
inf = 1000001
arr = [inf]*N
arr[0] = 0

for i in range(N):
    for j in range(i):
        power = (i-j) * (1+ abs(stone[i]-stone[j]))
        arr[i] = min(arr[i],max(arr[j], power))

print(arr[N-1])
#이해 완