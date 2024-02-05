import sys

input = sys.stdin.readline
_, m = map(int, input().split())
trees = list(map(int, input().split()))

def bi_search(m, trees):
    lo, hi = 0, max(trees)
    while lo < hi:
        h = 1 + lo + (hi - lo) // 2
        if sum(tree - h for tree in trees if tree > h) >= m:
            lo = h
        else:
            hi = h - 1

    return hi

print(bi_search(m, trees))