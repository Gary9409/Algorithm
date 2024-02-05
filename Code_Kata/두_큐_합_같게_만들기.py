# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    length = (len(q1) - 1) * 3
    
	# queue는 FIFO방식이므로 값을 계속 교환하더라도 전체 수열의 순서는 변하지 않는다.
    # (고정된 원형 큐에서 포인터 두 개가 원형 큐를 두 개의 큐로 나누는 형태로 생각)
    # 그러므로 가능한 모든 형태 중 최대 시행 횟수는 [1, 1, 1, 1], [1, 1, 7, 1] 같은 형태일 때
    # 2번 큐에서 n - 1번 pop, 다시 1번큐에서 2n - 2번 pop하는 경우이므로 최대 횟수는
    # n - 1 + n + n - 2 = 3(n - 1)번이 된다.
    while answer <= length:
        if s1 == s2:
            return answer
        
        if s1 > s2:
            i = q1.popleft()
            q2.append(i)
            s1 -= i
            s2 += i
        else:
            i = q2.popleft()
            q1.append(i)
            s1 += i
            s2 -= i
        
        answer += 1
    
    return answer if s1 == s2 else -1


queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]
# result = 2
print(f'#1\nqueue1 = {queue1}\nqueue2 = {queue2}\nresult = {solution(queue1, queue2)}\n')

queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
# result = 7
print(f'#2\nqueue1 = {queue1}\nqueue2 = {queue2}\nresult = {solution(queue1, queue2)}\n')

queue1, queue2 = [1, 1], [1, 5]
# result = -1
print(f'#3\nqueue1 = {queue1}\nqueue2 = {queue2}\nresult = {solution(queue1, queue2)}')