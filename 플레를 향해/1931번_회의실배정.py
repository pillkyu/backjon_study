import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
meeting = []

for i in range(n):
    meeting.append(list(map(int, input().split())))
meeting.sort()
dp = deque()
dp.append(meeting[0])
for k in range(1,n):
        if dp[-1][1]>meeting[k][1]:
            dp.pop()
            dp.append(meeting[k])
        elif dp[-1][1]<=meeting[k][0] or meeting[k][0] == meeting[k][1]:
            dp.append(meeting[k])
print(len(dp))