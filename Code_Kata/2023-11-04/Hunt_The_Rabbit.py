# https://www.acmicpc.net/problem/13777
import sys

def binary_search(rabbit):
    lo, hi = 1, 50
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(mid, end=' ')
        if mid > rabbit:
            hi = mid - 1
        elif mid < rabbit:
            lo = mid + 1
        else:
            print()
            break

while True:
    rabbit = int(sys.stdin.readline())
    if rabbit == 0:
        break
    binary_search(rabbit)