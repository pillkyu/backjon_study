import sys
def solve(n):
    arr =[]
    if n == 0:
        return 1
    for i in range(n):
        if i == 0:
            arr.append(1)
        elif i == 1:
            arr.append(3)
        else:
            arr.append(arr[i-1]+2*arr[i-2])
    return arr[-1]

while True:
    try:
        n = int(sys.stdin.readline())
        print(solve(n))
    except:
        break
