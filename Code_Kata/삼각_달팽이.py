# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    # 삼각형모양 2차원 배열 생성
    answer = [[None for _ in range(m + 1)] for m in range(n)]

    xset = (0, 1, -1)
    yset = (1, 0, -1)
    x, y, cnt = 0, -1, 0
    
    for i in range(n):
        # x, y의 진행방향과 반복횟수 설정
        dx, dy, t = xset[i % 3], yset[i % 3], n - i
        for _ in range(t):
            # 설정한 값만큼 반복하며 2차원 배열을 채워넣음
            x += dx
            y += dy
            cnt += 1
            answer[y][x] = cnt
            
	# 2차원 배열을 1차원 배열로 풀어서 반환
    return [num for lst in answer for num in lst]


n = 4
# result = [1,2,9,3,10,8,4,5,6,7]
print(f'#1\nn = {n}\nresult = {solution(n)}\n')

n = 5
# result = [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(f'#2\nn = {n}\nresult = {solution(n)}\n')

n = 6
# result = [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
print(f'#3\nn = {n}\nresult = {solution(n)}')