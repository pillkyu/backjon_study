N = int(input())
count = 0
total = 0

def happy_num(num):
    used_num = set()
    while num != 1 and num not in used_num:
        used_num.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1
for num in range(1, N+1):
    if happy_num(num):
        count += 1
        total += num

print(count, total)

