import sys

s = sys.stdin.readline().strip()

def min_sum(s):
    ret = 0
    sub = s.split('-')
    ret += sum(map(int, sub[0].split('+')))
    for s in sub[1:]:
        ret -= sum(map(int, s.split('+')))

    return ret

print(min_sum(s))