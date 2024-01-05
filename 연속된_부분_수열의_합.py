# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    lo, hi, sums = 0, 0, 0
    answer = [0, len(sequence)]
    
    while hi < len(sequence):
		
		# sums에 hi가 가리키는 원소 더하기
        sums += sequence[hi]
        
		# sums가 k보다 크면 0번부터 하나씩 빼기
        while sums > k:
            sums -= sequence[lo]
            lo += 1
        
		# lo, hi 전부 조작한 후 sums가 k면 구간 길이 비교 후 answer 갱신
        if sums == k:
            answer = min(answer, [lo, hi], key=lambda x: x[1] - x[0])
        
		# hi 포인터를 한 칸 옮김
        hi += 1
            
    return answer


sequence, k = [1, 2, 3, 4, 5], 7
# result = [2, 3]
print(f'#1\nsequence = {sequence}\nk = {k}\nresult = {solution(sequence, k)}\n')

sequence, k = [1, 1, 1, 2, 3, 4, 5], 5
# result = [2, 3]
print(f'#21\nsequence = {sequence}\nk = {k}\nresult = {solution(sequence, k)}\n')

sequence, k = [2, 2, 2, 2, 2], 6
# result = [2, 3]
print(f'#3\nsequence = {sequence}\nk = {k}\nresult = {solution(sequence, k)}')