import sys
from collections import defaultdict
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
belt = list(int(input()) for _ in range(n))
# 첫번쨰 풀이
# answer = 0
# for start in range(n):
#     if start+k<=n:
#         slice = set(belt[start:start+k]+[c])
#     else:
#         slice = set(belt[start:n]+belt[0:k-(n-start)]+[c])
#     answer = max(answer, len(slice))
# print(answer)

# 두 번쨰 풀이
# window = belt[:k]
# answer = len(set(window + [c]))
# for i in range(1,n):
#     end = i+k
#     if end>n:
#         end -= n
#     window.pop(0)
#     window.append(belt[end-1])
#     answer = max(answer, len(set(window + [c])))
# print(answer)

count = defaultdict(int)
answer = 0
unique = 0

# 초기 윈도우
for i in range(k):
    if count[belt[i]] == 0:
        unique += 1
    count[belt[i]] += 1

# 쿠폰 포함 여부
answer = unique + (0 if count[c] else 1)

# 슬라이딩 윈도우 시작
for i in range(1, n):
    # 윈도우 맨 앞 제거
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1

    # 윈도우 맨 뒤 추가 (회전 벨트)
    right = belt[(i + k - 1) % n]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    # 쿠폰 고려
    current = unique + (0 if count[c] else 1)
    answer = max(answer, current)

print(answer)