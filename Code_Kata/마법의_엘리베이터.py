# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    
	# storey를 최대값으로 설정
    answer = storey
    
    def dfs(num, cnt):
        nonlocal answer
	
		# 탐색 종료 조건
        if num == 0:
            answer = min(answer, cnt)
            return
	
		# 백트래킹 pruning 조건
        if cnt > answer:
            return
        
		# 0으로 내리는 가지와 10으로 올리는 가지로 dfs 탐색
        q, r = divmod(num, 10)
        dfs(q, cnt + r)
        dfs(q + 1, cnt + 10 - r)
    
    dfs(storey, 0)
    
    return answer


storey = 16
# result = 6
print(f'#1\nstorey = {storey}\nresult = {solution(storey)}\n')

storey = 2554
# result = 16
print(f'#2\nstorey = {storey}\nresult = {solution(storey)}\n')