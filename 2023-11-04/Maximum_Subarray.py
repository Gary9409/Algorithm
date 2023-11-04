# https://leetcode.com/problems/maximum-subarray/
from typing import List


# 배열에 n번째 요소가 들어왔을 때 해당 노드가 포함된 맥시멈 서브배열을 구하려면,
# f(n) = max(f(n - 1) + n, n) 과 같은 점화식을 사용하면 된다.
# n-1요소가 포함된 맥시멈 서브배열보다 n의 값이 더 크다면 기존의 서브배열을 버리고 n으로 시작하는 배열을 택하는 방식이다.
# 계산을 좀 더 최적화하기 위해 만약 f(n - 1)이 음수면,
# 즉 기존의 서브배열의 합이 0보다 낮다면 현재 노드값이 무조건 더 커지므로 계산에서 제외한다.
class Solution:
    # Tabulation
    def maxSubArray_tab(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

    # Memoization
    def maxSubArray_memo(self, nums: List[int]) -> int:
        table = [None] * len(nums)

        def dp(i):
            n = len(nums)
            if i == 0:
                table[i] = nums[i]
                return table[i]

            if table[i]:
                return table[i]

            table[i] = max(nums[i], dp(i - 1) + nums[i])
            return table[i]

        dp(len(nums) - 1)
        return max(table)

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print('Tabulation:', sol.maxSubArray_tab(nums.copy()))
print('Memoization:', sol.maxSubArray_memo(nums.copy()))