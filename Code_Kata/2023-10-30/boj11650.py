import sys

nums = []
for _ in range(int(sys.stdin.readline())):
    nums.append(tuple(map(int, sys.stdin.readline().split())))
for i, j in sorted(nums):
    print(f'{i} {j}')