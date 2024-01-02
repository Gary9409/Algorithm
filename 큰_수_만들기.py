# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = list()
	
    for n in number:

		# k개에 한해서 탐색하는 수가 현재까지 통과한 수보다 작아질 때 까지 제거
        while k and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        
        stack.append(n)
        
	# for문 통과후에도 k가 남아있으면 끝에서부터 제거
    while k:
        stack.pop()
        k -= 1
    
    return ''.join(stack) if stack[0] != '0' else 0


number, k = "1924", 2
# result = "94"
print(f'#1\nnumber = {number}, k = {k}\nresult = {solution(number, k)}\n')

number, k = "1231234", 3
# result = "3234"
print(f'#2\nnumber = {number}, k = {k}\nresult = {solution(number, k)}\n')

number, k = "4177252841", 4
# result = "775841"
print(f'#3\nnumber = {number}, k = {k}\nresult = {solution(number, k)}')