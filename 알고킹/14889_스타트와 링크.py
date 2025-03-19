import sys
input = sys.stdin.readline
N = int(input())
answer = 1e9
limit = N //2
s = []
start_link = [list(map(int, input().split())) for _ in range(N)]
def dfs(start):
    global s, answer
    if len(s) == limit:
        arr = [n for n in range(N)]
        vs = [n for n in arr if n not in s]
        answer = min(answer,abs(calc(s)-calc(vs)))
        return
    for i in range(start,N):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

def calc(s):
    cap = 0
    for i in s:
        for j in s:
            if i!=j:
                cap += start_link[i][j]
    return cap
dfs(0)
print(answer)






