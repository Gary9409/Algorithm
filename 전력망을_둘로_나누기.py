# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict

def solution(n, wires):
    answer = n
    
	# 완전탐색으로 서브트리 노드의 갯수를 반환
    def dfs(graph, root):
        stack, visited = [root], set()
        
        while stack:
            cur = stack.pop()
            
            if cur in visited:
                continue
            
            visited.add(cur)
            stack.extend(list(graph[cur]))
        
        return len(visited)
            
    
	# wires로 그래프 생성
    graph = defaultdict(set)
    for wire in wires:
        p, q = wire
        graph[p].add(q)
        graph[q].add(p)

	# 생성한 그래프에서 wire를 하나씩 제거한 후 dfs 탐색
    for wire in wires:
        p, q = wire
        tmp = []
        graph[p].remove(q)
        graph[q].remove(p)

		# 해당 wire가 제거되었을 때 생기는 두 서브트리의 노드 갯수 차이가 최소가 되도록 answer 갱신
        answer = min(answer, abs(dfs(graph, wire[1]) - dfs(graph, wire[0])))
        
        graph[p].add(q)
        graph[q].add(p)
        
    return answer


n, wires = 9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# result = 3
print(f'#1\nn = {n}\nwire = {wires}\nresult = {solution(n, wires)}\n')

n, wires = 4, [[1,2],[2,3],[3,4]]
# result = 0
print(f'#2\nn = {n}\nwire = {wires}\nresult = {solution(n, wires)}\n')

n, wires = 7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
# result = 1
print(f'#3\nn = {n}\nwire = {wires}\nresult = {solution(n, wires)}')