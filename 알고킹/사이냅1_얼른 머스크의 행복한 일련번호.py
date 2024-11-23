# 범위값을 받은 후 각 값을 분해한 후 제곱수로 더하는 것을 반복
# 중요한건 제곱수가 같은 값으로 순환하는지를 판단하는 것이기 때문에 이를 파악할 방법을 마련해야 한다고 생각함
N = int(input())
count = 0
total = 0

def happy_number(num):
    used_num = set() #순환한것을 판단하기 위한 set 정의
    while num != 1 and num not in used_num:
        used_num.add(num)
        num = sum(int(digit) ** 2 for digit in str(num)) #각 수를 분해 후 제곱
    return num == 1

for num in range(1, N + 1):
    if happy_number(num):
        count += 1
        total += num
print(f"1부터 {N} 범위의 행복 수는 {count}개이고 총합은 {total}입니다")



