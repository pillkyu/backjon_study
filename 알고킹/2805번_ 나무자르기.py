import sys
input = sys.stdin.readline
n,m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
while start <= end:
    answer = 0

    cut = (start + end) // 2
    for tree in trees:
        if tree >= cut:
            answer += tree-cut
        else:
            continue

    if answer > m:
        result = cut
        start = cut+1
    elif answer == m:
        result  = cut
        break

    elif answer < m:
        end = cut-1

print(result)
'''
이진탐색을 이용한 문제. 
처음 접근방식으로 가장 큰값을 기준으로 나눠서 진행하였으나 쓸데없는 과정을 너무 많이 추가하여
코드가 정상적으로 작동하지 않음. 
결론: 이진탐색은 이렇게 푸는게 그냥 정답이다.
근데 이 문제에서 좀 더 빠른 방법은 answer이 m하고 같을때 끝내는건데 의미가 없네요.
'''