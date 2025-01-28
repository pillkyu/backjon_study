import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(float, input().split())) for _ in range(N)]
blue_paper = 0
white_paper= 0
divide = N
while divide >0:
    for col in range(N//divide):
        for row in range(N//divide):
            start_col = col*divide
            start_row = row*divide
            save = list()
            hap = 0
            for i in range(start_col,start_col+divide):
                for j in range(start_row, start_row+divide):
                        hap += paper[i][j]
                        save.append((i,j))
            if hap == divide**2 or hap == 0:
                if hap == 0:
                    white_paper += 1
                else:
                    blue_paper += 1
                for code in save:
                    k,l = code
                    paper[k][l] = 0.001
    divide = divide//2

print(white_paper)
print(blue_paper)

