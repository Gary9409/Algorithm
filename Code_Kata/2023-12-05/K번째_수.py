import sys
from pprint import pprint

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# k의 최대값이 10억이므로 binary search 활용
def bi_search(n, k):
    # b[k]의 최대값은 모든 경우 대해 k보다 같거나 작으므로 최대값을 k로 잡는다.
    lo, hi = 1, k

    while lo < hi:
        mid = lo + (hi - lo) // 2
        count = 0
        # 각 row에 대해 mid보다 작거나 같은 값의 갯수를 구한다
        for i in range(1, n + 1):
            count += min(mid // i, n)

        print(count, mid)
        if count < k:
            lo = mid + 1
        else:
            hi = mid

    return lo

print(bi_search(n, k))