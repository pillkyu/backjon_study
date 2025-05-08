import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
city_go = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))

for middle in range(N):
    for col in range(N):
        for row in range(N):
            if city_go[col][middle] and city_go[middle][row]:
                city_go[col][row] = 1
for i in range(N):
    city_go[i][i] = 1

start = travel_plan[0]-1
flag = True
for i in range(1, len(travel_plan)):
    x = travel_plan[i]-1
    if city_go[start][x] == 0:
        flag = False
        break
    start = x
if flag:
    print("YES")
else:
    print("NO")
