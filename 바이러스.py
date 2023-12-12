# https://www.acmicpc.net/problem/2606

import sys
from collections import defaultdict

input = sys.stdin.readline
graph = defaultdict(list)
n = int(input())
for _ in range(int(input())):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

def dfs(graph):
    stack = [1]
    visited = set()

    while stack:
        cur = stack.pop()

        if cur in visited:
            continue

        visited.add(cur)
        stack.extend(graph[cur])

    return len(visited) - 1

print(dfs(graph))