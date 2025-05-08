import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
feed_tree = [list(map(int, input().split())) for _ in range(N)]
ground = [[5]*N for _ in range(N)]
forest =[[[] for _ in range(N)]for _ in range(N)]
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
answer = 0

for _ in range(M):
    x,y,z = map(int, input().split())
    forest[y-1][x-1].append(z) # 기본 나무 심기
    #forest에 나무 심어져있음


for _ in range(K):
    for y in range(N):
        for x in range(N):
            forest[y][x].sort()
            alive = []
            dead = 0

            for tree in forest[y][x]:
                if ground[y][x] >= tree:
                    ground[y][x] -= tree
                    alive.append(tree + 1)
                else:
                    dead += tree
            ground[y][x] += dead
            forest[y][x] = alive

    for y in range(N):
        for x in range(N):
            for tree in forest[y][x]:
                if tree >= 5 and tree %5 == 0:
                    for i in range(8):
                        ndy = y + dy[i]
                        ndx = x + dx[i]
                        if 0<=ndx<N and 0<=ndy<N:
                            forest[ndy][ndx].insert(0, 1)
    for y in range(N):
        for x in range(N):
            ground[y][x] += feed_tree[y][x]

for row in forest:
    for col in row:
        answer += len(col)

print(answer)

#si발 시간초과
