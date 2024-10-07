#22871번 징검다리 건너기(large)
import sys
input = sys.stdin.readline
N = int(input())


answer = 0
point = 0

arr = list(map(int, input().split()))
for i in range(N):
    if point > i:
        continue
    else:
        result = float("inf") 
        for j in range(i+1,N):
            jump = (j-i) * (1+abs(arr[i]-arr[j]))
            if jump < answer:
                answer = jump
                point = j
            else:
                continue
        answer += result
print(answer)