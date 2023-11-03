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

# 플로이드-워셜 알고리즘 사용시 메모리가 초과되므로 다른 알고리즘을 사용
def floyd_warshall(graph, V):
    dist = [[INF] * (V + 1) for _ in range(V + 1)]
    for i in range(1, V + 1):
        dist[i][i] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist

dist = floyd_warshall(graph, V)
for i in range(1, V + 1):
    print(dist[1][i]) if dist[1][i] != int(1e9) else print('INF')