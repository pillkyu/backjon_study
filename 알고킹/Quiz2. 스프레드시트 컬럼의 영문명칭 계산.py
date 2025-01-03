N = int(input())
alpabet = [chr(i) for i in range(65, 91)] #알파벳 리스트 정의

#먼저 해당 숫자를 알파벳으로 치환하기 위해 필요한 칸수를 계산.
#각 칸에 해당하는 26의 제곱수를 나눈 몫이고, 제곱 해야할 수는  ...2,1,0 처럼 내림차순으로 정렬되어야 한다.
box = []
square_num = 0
answer = N

#총 몇 칸이 필요한지 계산
while True:
    if answer >26:
        answer= answer // 26
        box.append(square_num)
        square_num += 1 #각 칸에 26에 몇제곱을 해야하는지를 미리 입력
    else:
        box.append(square_num)
        break

box.reverse() #앞에 있는 수가 제일 큰 제곱수를 계산해야하므로 역수로 만들어줌

#입력된 값을 26의 제곱수로 순서대로 나눈 후, 해당 값을 바로 알파벳으로 전환
for element in box:
    if element == 0: #해당하는 셀이 0일경우는 N값 그대로 사용
        element = alpabet[N-1]
    else:
        pow_num = element
        element = alpabet[N // (26 ** pow_num)-1]
        N = N %(26 ** pow_num)

    print(element, end = '')

