N = int(input())
alpabet = [chr(n) for n in range(65, 91)]

box = []
square_num = 0
answer = N

while True:
    if answer >26:
        answer = answer //26
        box.append(square_num)
        square_num += 1
    else:
        box.append(square_num)
        break
box.reverse()

for element in box:
    if element == 0:
        element = alpabet[N-1]
    else:
        pow_num = element
        element = alpabet[N//(26**pow_num)-1]
        N = N %(26 ** pow_num)
    print(element, end = '')
