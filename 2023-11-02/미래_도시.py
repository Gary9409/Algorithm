import sys
from dijkstra import Dijkstra

CASE_NUMBER = 1
with open(f'testcase/미래_도시_case{CASE_NUMBER}.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        p, q = map(int, input().split())
        graph[p].append((q, 1))
        graph[q].append((p, 1))
    x, k = map(int, input().split())

d = Dijkstra(graph)
path1, path2 = d.dijkstra(1)[k], d.dijkstra(k)[x]
if path1 != Dijkstra.INF and path2 != Dijkstra.INF:
    print(path1 + path2)
else:
    print(-1)