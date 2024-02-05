import sys

nums = []
for _ in range(int(sys.stdin.readline())):
    nums.append(tuple(map(int, sys.stdin.readline().split())))
for i, j in sorted(nums, key=lambda x: (x[1], x[0])):
    print(f'{i} {j}')