import sys
input = sys.stdin.readline
N,M = map(int, input().split())
n_list = list(map(int, input().split()))
for i in range(1,len(n_list)):
    n_list[i] = n_list[i-1]+n_list[i]
answer = [0]*M
for j in range(M):
    fir, sec = map(int, input().split())
    fir -= 1
    sec -= 1
    if fir == 0:
        answer[j] = n_list[sec]
    else:
        answer[j] = n_list[sec]-n_list[fir-1]


for ans in answer:
    print(ans)
