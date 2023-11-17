import sys
import collections

input = sys.stdin.readline

def josephus_seq(seq, target):
    deq = collections.deque(range(1, seq+ 1))
    ret = []

    while deq:
        deq.rotate(1 - target)
        ret.append(deq.popleft())

    return ret

log = josephus_seq(*map(int, input().split()))
print('<', end='')
print(*log, sep=', ', end='')
print('>')