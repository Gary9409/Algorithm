# https://www.acmicpc.net/problem/1654
import sys

k, n = map(int, sys.stdin.readline().split())
cables = []
for _ in range(k):
    cables.append(int(sys.stdin.readline()))

def solution(cables, n):
    lo, hi = 1, max(cables)
    while lo < hi:
        # 1 // 2 == 0이므로 mid가 움직이지 않는 것을 막기 위해 1씩 보정
        mid = 1 + lo + (hi - lo) // 2
        if sum(l // mid for l in cables) < n:
            # 현재 mid는 범위에 포함되지 않으므로 mid - 1
            hi = mid - 1
        else:
            # 현재 mid는 범위에 포함되므로 그대로
            lo = mid
    return hi

print(solution(cables, n))