# https://www.acmicpc.net/problem/4485
import heapq
import sys
from collections import defaultdict


# 런타임을 줄이기 위해 누적 루피를 저장하는 rupees를 만들어 사용
# 런타임(PyPy) 252ms
def dijkstra(graph):
    N = len(graph)
    rupees = [[INF] * N for _ in range(N)]
    rupees[0][0] = graph[0][0]

    pq = [(graph[0][0], (0, 0))]
    visited = set()

    while pq:
        rupee, pos = heapq.heappop(pq)

        # 현재 노드가 이미 방문한 노드일 때 처리
        if pos in visited:
            continue
        visited.add(pos)

        # 상하좌우의 좌표를 계산하여 가능한 경로일 경우 우선순위 큐에 추가
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx, ny = pos[0] + dx[i], pos[1] + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            # 누적 루피를 저장해둔 rupees와 비교하여 값이 클 경우 제외
            if rupee + graph[nx][ny] < rupees[nx][ny]:
                rupees[nx][ny] = rupee + graph[nx][ny]
                heapq.heappush(pq, (rupee + graph[nx][ny], (nx, ny)))

    return rupees

INF = int(1e9)
input = sys.stdin.readline
num = 1

while True:
    N = int(input())
    if N == 0:
        break

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(f'Problem {num}: {dijkstra(graph)[N - 1][N - 1]}')
    num += 1