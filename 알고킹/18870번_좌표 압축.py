import sys
import heapq
input = sys.stdin.readline
N = int(input())

X= list(map(int, input().split()))
sorted_set = sorted(set(X))
index_dict = {value : i for i, value in enumerate(sorted_set)}
print(' '.join(str(index_dict[x]) for x in X))




