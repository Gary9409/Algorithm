import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

def dfs(graph, v):
    stack = [v]
    visited = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.append(node)
        stack.extend(sorted(graph[node], reverse=True))

    return visited

def bfs(graph, v):
    q = deque([v])
    visited = []

    while q:
        node = q.popleft()

        if node in visited:
            continue

        visited.append(node)
        q.extend(sorted(graph[node]))

    return visited

print(*dfs(graph, v), sep=" ")
print(*bfs(graph, v), sep=" ")