# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    
    for n in numbers:
        
		# 짝수면 마지막 비트가 0이므로 1 더함
        if n % 2 == 0:
            answer.append(n + 1)
            continue
        

		# 홀수면 가장 뒤에 오는 0을 찾은 후, 0과 그 뒤 1을 교체
        binary, digit = bin(n), 0
        
        for bit in binary[::-1]:
            if bit == '0' or bit == 'b':
                break
            digit += 1
        
        answer.append(n + 2 ** digit - 2 ** (digit - 1))
        
    return answer


numbers = [2, 7]
# result = [3, 11]
print(f'#1\nnumbers = {numbers}\nresult = {solution(numbers)}\n')