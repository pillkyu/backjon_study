import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
not_heard = set(input() for _ in range(n))
not_seen = set(input() for _ in range(m))

# 교집합 찾기
result = sorted(not_heard & not_seen)  # 교집합 후 정렬
print(len(result))
for name in result:
    print(name, end = '')
