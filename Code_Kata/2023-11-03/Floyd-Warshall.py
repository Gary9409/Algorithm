import sys
from collections import defaultdict
from pprint import pprint

with open('testcase.fw') as f:
    sys.stdin = f
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

class FloydWarshall(graph):
    INF = int(1e9)
    def __init_(self):
        self.graph = graph

    def floyd_warshall(self):
        N = len(graph)
        dist = [[self.INF] * (N + 1) for _ in range(N + 1)]

        # 행, 열 번호가 같으면 0
        for idx in range(1, N + 1):
            dist[idx][idx] = 0

        # 그래프에서 경로와 거리를 가져와 입력
        for start, adjs in graph.items():
            for adj, d in adjs:
                dist[start][adj] = d

        # 입력한 데이터를 점화식에 대입
        # D_ab = min(D_ab, D_ak + D_kb)
        # 모든 그래프의 노드 k에 대하 a-b 거리와 a-k-b의 거리를 비교하는 방식
        for k in range(1, N + 1):
            for a in range(1, N + 1):
                for b in range(1, N + 1):
                    dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

        return dist