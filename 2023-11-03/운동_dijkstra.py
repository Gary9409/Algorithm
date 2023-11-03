# https://www.acmicpc.net/problem/1956
import heapq
import sys
from collections import defaultdict


INF = int(1e9)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 다익스트라 알고리즘을 전체 노드 갯수만큼 반복문을 돌려서 최소값을 구하는 방법
# 시간 초과
def dijkstra(graph, start):
    dist = defaultdict(lambda: int(1e9))
    pq = [(0, start)]
    visited = set()

    # # 사이클을 체크해야하므로 시작지점을 0으로 초기화지 않음
    # dist[start] = 0

    while pq:
        acc, cur = heapq.heappop(pq)

        if acc > 0 and cur == start:
            return acc
        if cur in visited:
            continue
        visited.add(cur)

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(pq, (cost, adj))

    return int(1e9)

cycle = int(1e9)
for i in range(1, V + 1):
    cycle = min(cycle, dijkstra(graph, i))
print(cycle) if cycle != int(1e9) else print(-1)