import sys
from collections import defaultdict
input = sys.stdin.readline
COM = int(input())
pair = int(input())
com_list = defaultdict(list)
virus_list = [0]*COM
virus_list[0] = 1
for i in range(pair):
    fir, sec = map(int, input().split())
    com_list[fir].append(sec)
    com_list[sec].append(fir)
def virus_dfs(start):
    for next_com in com_list[start]:
        if virus_list[next_com-1] == 0:
            virus_list[next_com-1] = 1
            virus_dfs(next_com)
virus_dfs(1)
print(sum(virus_list)-1)
