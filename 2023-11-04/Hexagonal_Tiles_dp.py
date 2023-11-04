# https://www.acmicpc.net/problem/5705
import sys


routes = [0] * 41
routes[0], routes[1], routes[2] = 1, 1, 2

# [f(0) == 1], f(1) == 1, f(2) == 2
# f(n) == f(n - 1) + f(n - 2)
def possible_routes(tiles):
    if tiles <= 2:
        routes[tiles] = tiles
        return tiles

    if routes[tiles] != 0:
        return routes[tiles]

    routes[tiles] = possible_routes(tiles - 1) + possible_routes(tiles - 2)
    return routes[tiles]

while True:
    tiles = int(sys.stdin.readline())
    if tiles == 0:
        break
    print(possible_routes(tiles))