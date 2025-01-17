import sys
input = sys.stdin.readline
n = int(input())
answer = [0]*(n+1)
answer[0] = 1
answer[1] = 3
def pivo(k):
    global answer
    if k == 1 or k ==2:
        return answer[k-1]
    else:
        for i in range(2,k):
            answer[i] = answer[i-1]+(answer[i-2]*2)
        return answer[k-1]
print(pivo(n)%10007)
