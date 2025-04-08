import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
cloud = [[0 for _ in range(n)] for _ in range(n)]
direction = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1], 5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1
cloud_direction = deque()

for _ in range(m):

