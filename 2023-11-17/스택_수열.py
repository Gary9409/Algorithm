import sys

input = sys.stdin.readline

def stack_seq(nums):
    stack = []
    seq = 1
    log = []

    for n in nums:
        while n >= seq:
            stack.append(seq)
            seq += 1
            log.append('+')
        if stack.pop() == n:
            log.append('-')
        else:
            print('NO')
            return

    print(*log, sep='\n')

nums = []
for _ in range(int(input())):
    nums.append(int(input()))
stack_seq(nums)