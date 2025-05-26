N  = int(input())
ball = list(input())
answer = 999999999
def count_color(start, color, back):
    count = 0
    if back ==0:
        for i in range(start, N):
            if ball[i] == color:
                count += 1
        return count
    elif back == 1:
        for j in range(start, -1, -1):
            if ball[j] == color:
                count += 1
        return count

for i in range(N):
    if ball[i] != 'R':
        answer = min(count_color(i,'R', 0), answer)
        break
for i in range(N):
    if ball[i] != 'B':
        answer = min(count_color(i,'B', 0), answer)
        break
for i in range(N-1,-1,-1):
    if ball[i] != 'R':
        answer = min(count_color(i, 'R', 1), answer)
        break
for i in range(N - 1, -1, -1):
    if ball[i] != 'B':
        answer = min(count_color(i, 'B', 1), answer)
        break
print(answer)