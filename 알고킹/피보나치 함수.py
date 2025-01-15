import sys
from functools import cache
input = sys.stdin.readline

@cache
def fibonacci(n):
    if n == 0:
        return (1, 0)  # (0의 개수, 1의 개수)
    elif n == 1:
        return (0, 1)
    else:
        prev2 = fibonacci(n-2)
        prev1 = fibonacci(n-1)
        return (prev1[0] + prev2[0], prev1[1] + prev2[1])

t = int(input())
for _ in range(t):
    n = int(input())
    zeros, ones = fibonacci(n)
    print(zeros, ones)