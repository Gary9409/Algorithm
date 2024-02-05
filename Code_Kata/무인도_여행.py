# https://school.programmers.co.kr/learn/courses/30/lessons/154540

import sys
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    xMax, yMax = len(maps) - 1, len(maps[0]) - 1
    maps = [[int(c) if c != 'X' else 0 for c in m] for m in maps]
    print(maps)
    
    def explore(x, y):
        nonlocal xMax, yMax

        if maps[x][y] == 0:
            return
        
        if maps[x][y] != 0:
            answer[-1] += maps[x][y]
            maps[x][y] = 0
        
        if x > 0:
            explore(x - 1, y)
        if x < xMax:
            explore(x + 1, y)
        if y > 0:
            explore(x, y - 1)
        if y < yMax:
            explore(x, y + 1)
            
    for i in range(xMax + 1):
        for j in range(yMax + 1):
            if maps[i][j]:
                answer.append(0)
                explore(i, j)

    return sorted(answer) if answer else [-1]


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
# result = [1, 1, 27]
print(f'#1\nmaps = {maps}\nresult = {solution(maps)}\n')

maps = ["XXX", "XXX", "XXX"]
# result = [-1]
print(f'#2\nmaps = {maps}\nresult = {solution(maps)}')