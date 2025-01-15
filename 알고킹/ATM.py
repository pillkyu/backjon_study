import sys
input = sys.stdin.readline

n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
answer = 0
for i in range(n):
    if i ==0:
        continue
    else:
        time_list[i] += time_list[i-1]
for time in time_list:
    answer += time
print(answer)
# answer = sum(time * (n-i) for i, time in enumerate(time_list))
#이런식으로도 가능하다