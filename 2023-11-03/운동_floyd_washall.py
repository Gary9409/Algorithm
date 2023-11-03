# https://www.acmicpc.net/problem/1956
import sys
from collections import defaultdict


INF = int(1e9)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 문제의 조건에서 노드의 갯수가 (2 <= V <= 400)이므로 플로이드-워셜 알고리즘을 사용해 볼 수 있다.
# CPython으로 제출시 타임오버, PyPy로 제출시 아슬아슬하게 오버되지 않은 것을 확인했다.
# 런타임(PyPy) 1304ms
def floyd_warshall(graph, V):
    dist = [[INF] * (V + 1) for _ in range(V + 1)]

    # # 사이클을 찾아야 하므로 자기 자신으로 돌아오는 경로를 0으로 초기화하지 않는다
    # for i in range(1, V + 1):
    #     dist[i][i] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist

dist = floyd_warshall(graph, V)
cycle = min([dist[i][i] for i in range(1, V + 1)])
print(cycle) if cycle != int(1e9) else print(-1)