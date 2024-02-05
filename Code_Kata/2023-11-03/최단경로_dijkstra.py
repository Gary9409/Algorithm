# https://www.acmicpc.net/problem/1753
import heapq
import sys
from collections import defaultdict


INF = int(1e9)
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 사용시 통과하는 것을 확인
# 런타임(PyPy) 520ms
def dijkstra(graph, V, K):
    dist = defaultdict(lambda: int(1e9))
    dist[K] = 0
    visited = set()
    pq = [(0, K)]

    while pq:
        acc, cur = heapq.heappop(pq)

        if cur in visited:
            continue
        visited.add(cur)

        for adj, d in graph[cur]:
            if acc + d < dist[adj]:
                dist[adj] = acc + d
                heapq.heappush(pq, (acc + d, adj))

    return dist

dist = dijkstra(graph, V, K)
print(*[dist[i] if i in dist else 'INF' for i in range(1, V + 1)], sep='\n')