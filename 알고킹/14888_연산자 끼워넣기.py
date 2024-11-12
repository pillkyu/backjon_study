import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
plus, minus,multi, divide  = map(int, input().split())
min_num = 1000000000
max_num = -1000000000
def dfs(plus, minus, multi, divide, cnt,answer):
    global min_num, max_num
    if cnt == len(A):
        min_num = min(min_num,answer)
        max_num = max(max_num, answer)
        return
    else:
        # 각 경우마다 새로운 계산 결과로 재귀 호출
        if plus > 0:
            dfs(plus - 1, minus, multi, divide, cnt+1, answer + A[cnt])
        if minus > 0:
            dfs(plus, minus - 1, multi, divide, cnt + 1, answer - A[cnt])
        if multi > 0:
            dfs(plus, minus, multi - 1, divide, cnt + 1, answer * A[cnt])

        if divide > 0:
            if answer < 0:
                dfs(plus, minus, multi, divide - 1, cnt + 1, -(-answer // A[cnt]))  # 음수 나눗셈 처리
            else:
                dfs(plus, minus, multi, divide - 1, cnt + 1, answer // A[cnt])

dfs(plus, minus, multi, divide, 1, A[0])

print(max_num)
print(min_num)
#dfs 굉장히 어렵군뇨
