import sys

n, c = map(int, sys.stdin.readline().split())
pos = [int(sys.stdin.readline()) for _ in range(n)]

# 좌표의 최대값이 10억이므로 이진 탐색 활용 (O(NlogN))
def bi_search(pos, c):
    # 좌표값을 정렬
    pos.sort()

    # '두 집 사이의 거리'를 이진 탐색으로 탐색한다.
    lo, hi = 1, pos[-1] - pos[0]

    # N = 2인 경우 두 집 사이의 거리가 최대값
    if len(pos) == 2:
        return hi

    while lo < hi:
        # 두 집 사이의 거리
        mid = 1 + lo + (hi - lo) // 2
        print(mid)

        # pos를 돌며 mid간격으로 배치할 수 있는 공유기 갯수 구함
        count, p = 1, pos[0]
        for i in range(len(pos)):
            if pos[i] - p >= mid:
                count += 1
                p = pos[i]

        # mid값 재설정
        if count >= c:
            lo = mid
        else:
            hi = mid - 1

    return lo

print(bi_search(pos, c))