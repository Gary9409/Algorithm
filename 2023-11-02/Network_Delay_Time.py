import collections
import heapq
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(start):
            dist = collections.defaultdict(lambda: int(1e9))
            pq = []
            heapq.heappush(pq, (0, start))
            dist[start] = 0
            visited = set()

            while pq:
                acc, cur = heapq.heappop(pq)

                if cur in visited:
                    continue
                visited.add(cur)
                # if dist[cur] < acc:
                #     continue

                for adj, d in graph[cur]:
                    cost = acc + d
                    if cost < dist[adj]:
                        dist[adj] = cost
                        heapq.heappush(pq, (cost, adj))

            return dist

        graph = collections.defaultdict(list)
        for p, q, d in times:
            graph[p].append((q, d))

        ret = dijkstra(k)
        return max(ret.values()) if len(ret) == n else -1

times = [[2,7,63],[4,3,60],[1,3,53],[5,6,100],[1,4,40],[4,7,95],[4,6,97],[3,4,68],[1,7,75],[2,6,84],
         [1,6,27],[5,3,25],[6,2,2],[3,7,57],[5,4,2],[7,1,53],[5,7,35],[4,1,60],[5,2,95],[3,5,28],[6,1,61],[2,5,28]]
n, k = 7, 3
sol = Solution()
print(sol.networkDelayTime(times, n, k))