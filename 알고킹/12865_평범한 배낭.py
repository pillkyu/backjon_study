import sys
input = sys.stdin.readline

N,K = int(input())
arr = []
for i in range(N):
    w,v = map(int, input())
    arr.append((w,v))

dp = [0]*N
for i in range(N):
