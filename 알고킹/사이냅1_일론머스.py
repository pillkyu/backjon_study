def is_happy_number(num):
    seen = set()  # 순환을 방지하기 위해 이미 나온 숫자를 기록
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))  # 각 자릿수의 제곱의 합 계산
    return num == 1  # num이 1이면 행복 수

N = 9999  # 1~9999 범위
happy_count = 0
happy_sum = 0

for num in range(1, N + 1):
    if is_happy_number(num):
        happy_count += 1
        happy_sum += num

print(f"행복 수의 개수: {happy_count}")
print(f"행복 수의 총합: {happy_sum}")
print(1441 * 7087069)


