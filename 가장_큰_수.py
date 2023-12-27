# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def solution(numbers):
    
    def sort_func(n, m):
        # 두 정수를 실제로 붙인 뒤 대소 비교하여 정렬
        return int(str(n) + str(m)) - int(str(m) + str(n))
    
	# 리스트 내 원소가 모두 0이면 '00...0'으로 나오기 때문에 예외처리
    res = ''.join(map(str, sorted(numbers, key=cmp_to_key(sort_func), reverse=True)))
    return '0' if res[0] == '0' else res


numbers = [6, 10, 2]
# result = 6210
print(f'#1\nnumbers = {numbers}\nresult = {solution(numbers)}\n')

numbers = [3, 30, 34, 5, 9]
# result = 9534330
print(f'#2\nnumbers = {numbers}\nresult = {solution(numbers)}')