# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):

    # bfs 사용
    # 중복방문하는 노드를 없애고 정답유무를 빠르게 체크하기 위해 큐 대신 set 사용
    answer, bfs = 0, {x}

    while bfs:
        if y in bfs:
            return answer
        nxt = set()

        for cur in bfs:
            nums = {cur + n, cur * 2, cur * 3}
            for i in nums:
                if i <= y:
                    nxt.add(i)

        bfs = nxt
        answer += 1

    return -1


x, y, n = 10, 40, 5
# result = 2
print(f'#1\nx, y, n = {x}, {y}, {n}\nresult = {solution(x, y, n)}\n')

x, y, n = 10, 40, 30
# result = 1
print(f'#2\nx, y, n = {x}, {y}, {n}\nresult = {solution(x, y, n)}\n')

x, y, n = 2, 5, 4
# result = -1
print(f'#3\nx, y, n = {x}, {y}, {n}\nresult = {solution(x, y, n)}')