# https://school.programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

	# 다익스트라 알고리즘 사용
    def dijkstra(graph):
        dist = defaultdict(lambda: int(1e9))
        dist[1] = 0
        visited = set()
        pq = [(0, 1)]
        
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

    time = dijkstra(graph)
    for t in time.values():
        if t <= K:
            answer += 1
            
    return answer


N, K = 5, 3
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# result = 4
print(f'#1\nN, K = {N}, {K}\nroad = {road}\nresult = {solution(N, road, K)}\n')

N, K = 6, 4
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# result = 4
print(f'#2\nN, K = {N}, {K}\nroad = {road}\nresult = {solution(N, road, K)}')