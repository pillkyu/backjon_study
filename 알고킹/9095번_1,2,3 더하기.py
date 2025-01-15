import sys
input = sys.stdin.readline
T = int(input())
def cnt(num):
    global count, n
    if num+1<=n:
        cnt(num+1)
    if num+2<=n:
        cnt(num+2)
    if num+3<=n:
        cnt(num+3)
    if num == n:
        count+=1

for i in range(T):
    count = 0
    n = int(input())
    cnt(0)
    print(count)
