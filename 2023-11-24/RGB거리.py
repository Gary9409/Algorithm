import heapq
import sys
input = sys.stdin.readline

cost = []
for _ in range(int(input())):
    cost.append(list(map(int, input().split())))

# 힙을 이용하여 풀이 -> 시간초과
def heap(cost):
    path = [(0, 0, '')]
    length = len(cost)

    while path:
        total, idx, rgb = heapq.heappop(path)

        # 마지막 집까지 계산했으면 최소금액 반환
        if idx >= length:
            return total

        # 현재 집의 가격 정보 가져옴
        r, g, b = cost[idx]

        # 전 집이 고른 지붕 색과 다른 색만 고를 수 있음
        # 이 집이 r을 고를 경우
        if (rgb != 'r'):
            path.append((total + r, idx + 1, 'r'))

        # 이 집이 g를 고를 경우
        if (rgb != 'g'):
            path.append((total + g, idx + 1, 'g'))

        # 이 집이 b를 고를 경우
        if (rgb != 'b'):
            path.append((total + b, idx + 1, 'b'))

# cost 테이블을 이용하여 dp -> 통과
def dp(cost):
    for i in range(1, len(cost)):
        # 현재 집에서 r을 골랐을 경우 최소값
        cost[i][0] += min(cost[i - 1][1], cost[i - 1][2])
        # 현재 집에서 g를 골랐을 경우 최소값
        cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])
        # 현재 집에서 b를 골랐을 경우 최소값
        cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])

    return min(cost[-1])

print(dp(cost))