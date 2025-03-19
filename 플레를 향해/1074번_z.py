import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())#r은 행, c는 열, n은 2**n행, 열의 바둑판

def find_rc(n, r, c):
    if n == 0:
        return 0
    size = 2**(n-1)
    area = size*size

    if c<size and r<size:
        return find_rc(n-1, r, c)
    elif c >= size and r<size:
        return area+find_rc(n-1, r, c-size)
    elif c<size and r>= size:
        return 2*area + find_rc(n-1, r-size, c)
    else:
        return 3*area + find_rc(n-1, r-size, c-size)
print(find_rc(n,r,c))
#정답지를 보고 품. 배열을 구현해서 풀려고 하였지만 그것도 실패했고 애초에 시간복잡도가 너무 높아지기 때문에 좋지 않음
#핵심은 사분면으로 나눈 후 해당 값을 재귀를 통해서 어느 사분면에 있는지를 구하고 현재의 위치에 해당하는 값만 구하는 것이 중요
#재귀문제를 좀 더 풀어보면서 감을 잡는 것이 중요할듯




