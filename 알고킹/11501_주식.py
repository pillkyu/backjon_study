import sys
input = sys.stdin.readline
T = int(input())
# for _ in range(T):
#     N = int(input())
#     stock = list(map(int, input().split()))
#     length = len(stock)
#     revenue = [0] * length
#     shop_list = [0] * length
#     answer = 0
#     shop_list[0] = stock[0]
#     for i in range(1,length):
#         shop_list[i] = stock[i]
#         if stock[i] > stock[i-1]:
#             for j in range(i):
#                 if shop_list[j] < stock[i]:
#                     revenue[j] = max(revenue[j], stock[i]-shop_list[j])
#     for n in revenue:
#         answer += n
#     print(answer)

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    length = len(stock)-1
    max_stock = 0
    answer = 0
    for i in range(length,-1,-1):
        if stock[i]>max_stock:
            max_stock = stock[i]
        else:
            answer += max_stock-stock[i]
    print(answer)

