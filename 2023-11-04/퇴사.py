# https://www.acmicpc.net/problem/14501
import sys


input = sys.stdin.readline
sch = []
N = int(input())
for _ in range(N):
    sch.append(tuple(map(int, input().split())))

MAX = 0
def dp(idx, pay):
    global MAX
    # 마지막 날에 도착하면 MAX값 비교 후 갱신
    if idx >= N:
        if pay > MAX:
            MAX = pay
        return

    # 스케쥴 표에서 기간과 금액 가져옴
    t, p = sch[idx]

    # 해당 날짜에 일을 하지 않을 경우
    dp(idx + 1, pay)

    #해당 날짜에 일을 할 경우
    if idx + t > N: return
    dp(idx + t, pay + p)

dp(0, 0)
print(MAX)