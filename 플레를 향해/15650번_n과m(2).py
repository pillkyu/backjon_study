'''
백트래킹 알고리즘을 활용
DFS를 구현하여 가능한 모든 경우의 수를 찾고 이 때 조건을 걸어
필요없는 해를 제외하고 다음 단계로 넘어가는 것
'''
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = [i for i in range(1,n+1)]
answer = list()

def DFS(choose, start):
    for i in range(start, len(arr)):
            choose.append(arr[i])
            if len(choose) == m:
                answer.append(choose[:])

            else:
                DFS(choose,i+1)
            choose.pop(-1)

DFS([], 0)

for row in answer:
    print(' '.join(map(str, row)))
'''
# 15650번
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
이게 찐 정답 코드
'''


