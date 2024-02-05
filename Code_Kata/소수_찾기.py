# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    
	# 소수 판별하는 함수
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True
    
	# 문자열 길이가 7 이하이므로 최대 13000개 정도의 순열이 나오므로 전체 순열을 구한 뒤 적당히 가공
    s = {int(''.join(map(str, n))) for digit in range(1, len(numbers) + 1) for n in permutations(numbers, digit)}
    
    for n in s:
        answer += isPrime(n)
    
    return answer


numbers = "17"
# result = 3
print(f'''#1\nnumbers = "{numbers}"\nresult = {solution(numbers)}\n''')

numbers = "011"
# result = 2
print(f'''#2\nnumbers = "{numbers}"\nresult = {solution(numbers)}\n''')