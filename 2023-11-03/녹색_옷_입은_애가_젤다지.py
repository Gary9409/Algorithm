# https://www.acmicpc.net/problem/4485
import heapq
import sys


# 출발 노드와 도착 노드가 고정되어 있으므로 따로 데이터를 저장하지 않고 동작하게 작성했다.
# 정답은 맞지만 최소값을 비교하지 않고 매번 힙소트로 해결하므로 런타임이 길어진다.
# 런타임(PyPy) 640ms
def solution(graph):
    N = len(graph)
    pq = [(graph[0][0], (0, 0))]
    visited = set()

    while pq:
        rupee, pos = heapq.heappop(pq)

        # 현재 좌표가 출구거나 방문했던 노드일 때 처리
        if pos == (N - 1, N - 1):
            return rupee
        if pos in visited:
            continue
        visited.add(pos)

        # # 다음 탐험할 노드 힙에 추가
        # if pos[0] > 0:
        #     x = pos[0] - 1
        #     y = pos[1]
        #     heapq.heappush(pq, (rupee + graph[x][y], (x, y)))
        # if pos[0] < N - 1:
        #     x = pos[0] + 1
        #     y = pos[1]
        #     heapq.heappush(pq, (rupee + graph[x][y], (x, y)))
        # if pos[1] > 0:
        #     x = pos[0]
        #     y = pos[1] - 1
        #     heapq.heappush(pq, (rupee + graph[x][y], (x, y)))
        # if pos[1] < N - 1:
        #     x = pos[0]
        #     y = pos[1] + 1
        #     heapq.heappush(pq, (rupee + graph[x][y], (x, y)))

        # 책을 참고하여 간결하게 수정
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx, ny = pos[0] + dx[i], pos[1] + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            # O(logN)
            heapq.heappush(pq, (rupee + graph[nx][ny], (nx, ny)))

    return -1

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
    print(f'Problem {num}: {solution(graph)}')
    num += 1