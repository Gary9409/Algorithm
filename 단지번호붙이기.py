# https://www.acmicpc.net/problem/2667

import sys

input = sys.stdin.readline
map, res = list(), list()
for _ in range(int(input())):
    map.append(list(input().strip()))

# 1을 만나면 단지의 내부를 탐색
def dfs(x, y):
    if map[x][y] == "1":
        res[-1] += 1
        map[x][y] = "0"
    else:
        return

    if x > 0:
        dfs(x - 1, y)
    if x < len(map) - 1:
        dfs(x + 1, y)
    if y > 0:
        dfs(x, y - 1)
    if y < len(map) - 1:
        dfs(x, y + 1)

# 왼쪽 위부터 지도를 탐색
def explore():
    for x in range(len(map)):
        for y in range(len(map)):
            if map[x][y] == "1":
                res.append(0)
                dfs(x, y)

explore()
print(len(res), *sorted(res), sep="\n")