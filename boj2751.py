import sys

nums = []
for _ in range(int(sys.stdin.readline())):
    nums.append(int(sys.stdin.readline()))
print(*sorted(nums), sep='\n')