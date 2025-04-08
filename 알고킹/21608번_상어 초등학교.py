import sys


input = sys.stdin.readline
N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
classroom = [[0 for _ in range(N)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0
for student in students:
    now = 0
    seat_list = [[-1,-1,N**2+1,N**2+1] for _ in range(N ** 2)]
    for y in range(N):
        for x in range(N):
            if classroom[y][x] == 0:
                for i in range(4):
                    ndx = x + dx[i]
                    ndy = y + dy[i]
                    if 0<=ndx<N and 0<=ndy<N:
                        for like in range(1,5):
                            if classroom[ndy][ndx] == student[like]:
                                seat_list[now][0] += 1
                        if classroom[ndy][ndx] == 0:
                            seat_list[now][1] += 1
                seat_list[now][2] = y
                seat_list[now][3] = x

            now += 1
    seat_list.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    best = seat_list[0]
    classroom[best[2]][best[3]] = student[0]
for student in students:
    for y in range(N):
        for x in range(N):

            if student[0] == classroom[y][x]:
                count = 0
                for i in range(4):
                    ndx = x + dx[i]
                    ndy = y + dy[i]
                    if 0<=ndx<N and 0<=ndy<N:
                        for like in range(1,5):
                            if classroom[ndy][ndx] == student[like]:
                                count += 1
                if count == 1:
                            answer += 1
                elif count == 2:
                            answer += 10
                elif count == 3:
                            answer += 100
                elif count == 4:
                            answer += 1000
                elif count == 0:
                            answer += 0

print(answer)







