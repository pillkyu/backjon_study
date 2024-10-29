import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    t, s = map(int, input().split())
    arr.append((s,t))
arr.sort()
start_time = arr[0][0]- arr[0][1]
end_time = arr[0][0]

for i in range(1, N):

            if arr[i][1]+ end_time > arr[i][0]:
                    start_time = start_time- (arr[i][1] + end_time - arr[i][0])
                    end_time = arr[i][0]
            else:
                    end_time += arr[i][1]
            if start_time < 0:
                        start_time = -1
                        break
print(start_time)

