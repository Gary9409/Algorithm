# https://leetcode.com/problems/house-robber/
from typing import List


# 집이 두 채 이하면 둘 중 돈이 많은 집을 선택하고,
# 셋 이상부터 f(n) = max(f(n - 2) + n, f(n - 1))의 점화식을 사용한다
# (2칸 이전 집까지의 최대금액 + 지금 집의 금액)과 (1칸 이전 집까지의 최대 금액)을 비교한다.
class Solution:
    # 상향식으로 해결한다
    def rob_tab(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        return nums[n - 1]

    # 메모 배열을 만들어 데이터를 저장하며 하향식으로 해결한다
    def rob_memo(self, nums: List[int]) -> int:
        acc = [None] * len(nums)
        def dp(addr):
            n = len(nums)
            if addr == n - 1:
                acc[addr] = nums[addr]
                return acc[addr]
            if addr == n - 2:
                acc[addr] = max(nums[addr], nums[addr + 1])
                return acc[addr]

            if acc[addr]:
                return acc[addr]

            if nums[addr] == 0:
                acc[addr] = dp(addr + 1)
            else:
                acc[addr] = max(nums[addr] + dp(addr + 2), dp(addr + 1))
            return acc[addr]

        return dp(0)

    # 모든 배열을 순회하며 최대 금액값을 갱신한다
    def rob_recur(self, nums: List[int]) -> int:
        max_money = 0
        def recur(addr, acc):
            nonlocal max_money
            n = len(nums)

            if addr >= n:
                max_money = max(max_money, acc)
                return

            money = nums[addr]

            recur(addr + 1, acc)
            recur(addr + 2, acc + money)

            return

        recur(0, 0)
        return max_money

sol = Solution()
nums = [2,7,9,3,1]
print('Tabulation:', sol.rob_tab(nums.copy()))
print('Memoization:', sol.rob_memo(nums.copy()))
print('Recursion:', sol.rob_recur(nums.copy()))