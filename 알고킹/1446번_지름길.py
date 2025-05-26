import sys
input = sys.stdin.readline
n, d = map(int, input().split())
road = [i for i in range(d+1)]
short_cut = []
for i in range(n):
    start, end, length = map(int, input().split())
    short_cut.append((start, end, length))
short_cut.sort()

k = 0
for i in range(d+1):
    road[i] = min(road[i-1]+1, road[i])
    while k<n:
        if i == short_cut[k][0]:
            if short_cut[k][1]<=d:
                road[short_cut[k][1]]=min(road[i]+short_cut[k][2],road[short_cut[k][1]])
            k += 1
        else:
            break
print(road[d])
