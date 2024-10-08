import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = []
answer = 1
point = 0
for _ in range(M):
    arr.append(int(input()))


def sort(i):
    num_list = []
    if i == 0:
        return 1
    for j in range(i):
        if j == 0:
            num_list.append(1)
        elif j == 1:
            num_list.append(2)
        else:
             num_list.append(num_list[j-1] + num_list[j-2])
    return  num_list[-1]




for i in arr:
    answer *= sort(i-point-1)
    point  = i
answer *= sort(N-point)
print(answer)







