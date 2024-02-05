# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
	# bridge_length 길이의 deque와 deque의 합을 나타낼 wsum 선언
    answer, bridge, wsum = 0, deque([0 for _ in range(bridge_length)], maxlen=bridge_length), 0
    
    for truck in truck_weights:
        
		# 다리 맨 앞 칸의 무게를 wsum에서 제거
        wsum -= bridge[0]
        
		# wsum + truck이 무게제한보다 높다면 반복
        while wsum + truck > weight:
            bridge.append(0)
            wsum -= bridge[0]
            answer += 1
        
		# 다리에 truck을 추가
        wsum += truck
        bridge.append(truck)
        answer += 1
        
    return answer + bridge_length


bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
# return = 8
print(f'#1\nbridge_length = {bridge_length}\nweight = {weight}\ntruck_weights = {truck_weights}\nresult = {solution(bridge_length, weight, truck_weights)}\n')

bridge_length, weight, truck_weights = 100, 100, [10]
# return = 101
print(f'#2\nbridge_length = {bridge_length}\nweight = {weight}\ntruck_weights = {truck_weights}\nresult = {solution(bridge_length, weight, truck_weights)}\n')

bridge_length, weight, truck_weights = 100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# return = 110
print(f'#3\nbridge_length = {bridge_length}\nweight = {weight}\ntruck_weights = {truck_weights}\nresult = {solution(bridge_length, weight, truck_weights)}\n')