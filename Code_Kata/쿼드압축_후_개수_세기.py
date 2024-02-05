# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    
	# 백트래킹
    def dfs(n, x, y):
        nonlocal answer
        
		# 한 변의 길이가 1이 되면 해당 값 개수 증가 후 리턴
        if n <= 1:
            answer[arr[y][x]] += 1
            return
        
		# 좌상단 값을 기준으로 모든 배열 순회
        target = arr[y][x]
        for i in range(x, x + n):
            for j in range(y, y + n):
                
                if arr[j][i] == target:
                    continue
                
				# 하나라도 값이 다르다면 배열을 4등분하여 다시 탐색
                n //= 2
                dfs(n, x, y)
                dfs(n, x + n, y)
                dfs(n, x, y + n)
                dfs(n, x + n, y + n)
                return
        
		# 전부 같다면 죄상단 값 개수 증가 후 리턴
        answer[target] += 1
        return

    dfs(len(arr), 0, 0)
    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# result = [4,9]
print(f'#1\narr = {arr}\nresult = {solution(arr)}\n')

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# result = [10, 15]
print(f'#2\narr = {arr}\nresult = {solution(arr)}\n')