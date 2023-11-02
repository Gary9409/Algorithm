import heapq


class Dijkstra:
    INF = int(1e9)
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start):
        N = len(self.graph)
        dist = [self.INF] * N

        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0

        while pq:
            acc, cur = heapq.heappop(pq)
            if dist[cur] < acc:
                continue

            for adj, d in self.graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(pq, (cost, adj))

        return dist

    def dijkstra_naive(self, start):
        def min_node():
            min_val = self.INF
            idx = 0
            for i in range(1, N):
                if dist[i] < min_val and not visited[i]:
                    min_val = dist[i]
                    idx = i
            return idx

        N = len(self.graph)
        visited = [False] * N
        dist = [self.INF] * N

        visited[start] = True
        dist[start] = 0

        for adj, d in self.graph[start]:
            dist[adj] = d

        for _ in range(N - 1):
            cur = min_node()
            visited[cur] = True
            for adj, d in self.graph[cur]:
                cost = dist[cur] + d
                if cost < dist[adj]:
                    dist[adj] = cost

        return dist