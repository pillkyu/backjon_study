from collections import deque
queue = deque()
answer =0
a = int(input('a값 입력:'))
b = int(input('b값 입력:'))
num = 0

def pivo(n):
    if n ==1 or n ==2:
        queue.append(1)
        return 1
    else:
        result = queue[0]+queue[1]
        queue.append(result)
        if len(queue)>2:
            queue.popleft()
        return result

while True:
    num += 1
    current = pivo(num)
    if a <= current and b >= current:
        answer += current  # 만약 조건에 부합하는 숫자일 경우 값을 더하고
    elif current > b:
        break  # b를 초과할 시 반복문 탈출
    else:
        continue
print(answer)