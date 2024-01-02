# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    answer = 0
    stack, cur = [], 1
        
    for i in order:
        
		# 메인 벨트의 상자가 원하는 번호가 될때까지 서브 벨트로 밀어넣음
        while cur < i:
            stack.append(cur)
            cur += 1
        
		# 만약 원하는 상자가 메인 벨트에 없고 서브 벨트에서도 꺼낼 수 없으면 즉시 종료
        if cur > i and stack and stack[-1] != i:
            break
        
		# 메인 벨트 혹은 서브 벨트에서 원하는 상자를 꺼낸 후 answer += 1
        if cur == i:
            cur += 1
        elif stack and stack[-1] == i:
            stack.pop()       
        answer += 1
    
    return answer


order = [4, 3, 1, 2, 5]
# result = 2
print(f'#1\norder = {order}\nresult = {solution(order)}\n')

order = [5, 4, 3, 2, 1]
# result = 5
print(f'#2\norder = {order}\nresult = {solution(order)}\n')