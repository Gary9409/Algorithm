# https://www.acmicpc.net/problem/5705
import sys


# 처음에 생각했던 풀이였는데 런타임이 너무 길어서 통과하지 못함
def possible_routes(tiles):
    stack = [0]
    routes = 0
    while stack:
        cur = stack.pop()
        if cur >= tiles:
            routes += (cur == tiles)
            continue
        stack.append(cur + 1)
        stack.append(cur + 2)

    return routes

while True:
    tiles = int(sys.stdin.readline())
    if tiles == 0:
        break
    print(possible_routes(tiles))