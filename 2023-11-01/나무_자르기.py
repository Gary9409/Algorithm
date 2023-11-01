# https://www.acmicpc.net/problem/2805
import sys

_, l = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def solution(trees, l):
    lo, hi = 0, max(trees)
    while lo < hi:
        mid = 1 + lo + (hi - lo) // 2
        # if sum(max(0, tree - mid) for tree in trees) < l:
        if sum(tree - mid for tree in trees if tree - mid > 0) < l:
            hi = mid - 1
        else:
            lo = mid

    return hi

print(solution(trees, l))