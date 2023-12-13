# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)

# 배추(1)를 찾으면 0으로 바꾸고 상하좌우 dfs
def dfs(x, y):
    if grid[x][y] == 1:
        grid[x][y] = 0
        if x > 0:
            dfs(x - 1, y)
        if x < len(grid) - 1:
            dfs(x + 1, y)
        if y > 0:
            dfs(x, y - 1)
        if y < len(grid[0]) - 1:
            dfs(x, y + 1)

def explore():
    count = 0
    # 밭을 돌면서 배추를 탐색
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # 배추를 찾으면 카운트를 1 올리고 dfs로 보냄
            if grid[i][j] == 1:
                count += 1
                dfs(i, j)

    return count

input = sys.stdin.readline
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    print(explore())