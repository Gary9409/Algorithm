import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    sqrt = int(d ** (1/2))
    count = sqrt * 2 - 1
    offset = d - sqrt * sqrt
    if offset > sqrt: count += 2
    elif offset > 0: count += 1
    print(count)