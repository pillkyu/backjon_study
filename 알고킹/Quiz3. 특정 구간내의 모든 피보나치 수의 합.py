from collections import deque
#피보나치 함수를 이용하는 간단한 문제로 a와 b 사이에 해당하는 피보나치 수열 값을 모두 더하면 된다.
#피보나치 함수를 진행할 때 사용되는 메모리와 시간값을 최대한 줄이기 위해 양방향 큐를 통해 구현

queue = deque()
answer =0
a = int(input('a값 입력:'))
b = int(input('b값 입력:'))
num = 0

#피보나치 함수 정의
def pivo(n):
    if n == 1 or n == 2:
        queue.append(1)
        return 1

    result = queue[0] + queue[1]
    queue.append(result)
    if len(queue) > 2: #피보나치 함수를 구할 때 전 항 두개만 있으면 계산 가능
        queue.popleft() #따라서 나머지 항을 지우도록 구현. 데큐가 일반 리스트보다 빠르게 지움
    return result

while True:
    num += 1
    current = pivo(num)
    if a<= current and b>= current:
        answer += current #만약 조건에 부합하는 숫자일 경우 값을 더하고
    elif current>b:
        break #b를 초과할 시 반복문 탈출
    else:
        continue
print(answer)

