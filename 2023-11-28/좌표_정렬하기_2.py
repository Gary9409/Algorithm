import sys

input = sys.stdin.readline

p = []
for _ in range(int(input())):
    p.append(tuple(map(int, input().split())))
p.sort(key=lambda x: (x[1], x[0]))
for tup in p:
    print(f"{tup[0]} {tup[1]}")