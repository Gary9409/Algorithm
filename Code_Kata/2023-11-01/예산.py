# https://www.acmicpc.net/problem/2512
import sys

_ = sys.stdin.readline()
budgets = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

def solution(budgets, total):
    if sum(budgets) <= total:
        return max(budgets)

    lo, hi = 0, max(budgets)
    while lo < hi:
        # 1 // 2 == 0이므로 mid가 움직이지 않는 것을 막기 위해 1씩 보정
        mid = 1 + lo + (hi - lo) // 2
        if sum(min(b, mid) for b in budgets) > total:
            # 현재 mid는 범위에 포함되지 않으므로 mid - 1
            hi = mid - 1
        else:
            # 현재 mid는 범위에 포함되므로 그대로
            lo = mid
    return hi

print(solution(budgets, total))