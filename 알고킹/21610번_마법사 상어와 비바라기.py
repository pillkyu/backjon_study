import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
current_row  = n-1
current_col = 0
cloud = [[0 for _ in range(n)] for _ in range(n)]
direction = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1], 5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
for _ in range(m):
    d, s = map(int, input().split())
    for _ in range(s):
        current_row = current_row+direction.get(d)[0]
        current_col = current_col+direction.get(d)[1]
    if current_row<0:
        current_row = n+current_row
    elif current_col<0:
        current_col = n+current_col

    A[current_col][current_row] +=1
    A[current_col][current_row+1] += 1
    A[current_col-1][current_row] += 1
    A[current_col-1][current_row+1] += 1

    for i in range(2,9,2):
        if A[current_row+direction.get(i)[0]][current_col+direction.get(i)[1]] > 0:
            A[current_col][current_row] += 1

    for i in range(2,9,2):
        if A[current_row+direction.get(i)[0]][current_col+1+direction.get(i)[1]] > 0:
            A[current_col][current_row+1] += 1
    for i in range(2,9,2):
        if A[current_row-1+direction.get(i)[0]][current_col+direction.get(i)[1]] > 0:
            A[current_col-1][current_row] += 1
    for i in range(2,9,2):
        if A[current_row-1+direction.get(i)[0]][current_col+1+direction.get(i)[1]] > 0:
            A[current_col-1][current_row+1] += 1

    for j in range(n):
        for k in range(n):
            if A[k][j]>0


