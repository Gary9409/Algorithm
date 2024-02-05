import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# def min_coins(k, coins):
#     ret = 0
#     coins.reverse()
#     for coin in coins:
#         if coin > k:
#             continue
#         tmp, k = divmod(k, coin)
#         ret += tmp
#         if k == 0:
#             return ret

def min_coins(k, coins):
    ret = 0
    for coin in coins[::-1]:
        if coin > k:
            continue
        ret += k // coin
        k = k % coin
        if k == 0:
            return ret

print(min_coins(k, coins))