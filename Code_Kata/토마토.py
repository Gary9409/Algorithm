# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
grid, zeros, q = list(), 0, deque()
for i in range(n):
    row = list(map(int, input().split()))
    zeros += row.count(0)
    q += [(i, j) for j, val in enumerate(row) if val == 1]
    grid.append(row)

def bfs(m, n, zeros):
    day = 0

    # 하루가 끝난 후 오늘 익은 토마토를 큐에 추가
    while q:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            # 상하좌우 토마토 확인 후 익지 않았으면 익힌 후 큐에 추가
            if x > 0 and grid[x-1][y] == 0:
                grid[x-1][y] = 1
                zeros -= 1
                q.append((x-1, y))
            if x < n - 1 and grid[x+1][y] == 0:
                grid[x+1][y] = 1
                zeros -= 1
                q.append((x+1, y))
            if y > 0 and grid[x][y-1] == 0:
                grid[x][y-1] = 1
                zeros -= 1
                q.append((x, y-1))
            if y < m - 1 and grid[x][y+1] == 0:
                grid[x][y+1] = 1
                zeros -= 1
                q.append((x, y+1))

    # 익지 않은 토마토가 남았으면 -1, 다 익었으면 날짜 반환
    return day - 1 if zeros == 0 else -1

print(bfs(m, n, zeros))