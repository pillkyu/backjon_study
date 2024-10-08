import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

step = [0]*N
if len(arr)<=2:
    print(sum(arr))
else:
    step[0] = arr[0]
    step[1] = arr[1]+arr[0]
    step[2] = max(arr[2]+arr[1], arr[0]+arr[2])
    for i in range(3, N):
        step[i] = max(arr[i]+step[i-2], arr[i]+arr[i-1] + step[i-3])
    print(step[-1])


