import sys

input = sys.stdin.readline
_, sum = map(int, input().split())
nums = list(map(int, input().split()))

def black_jack(nums, sum):
    maxSum = 0
    nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tmp = nums[i] + nums[j] + nums[k]
                if tmp > sum:
                    break
                elif tmp == sum:
                    return tmp
                maxSum = max(maxSum, tmp)

    return maxSum

print(black_jack(nums, sum))