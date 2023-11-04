# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        # Memoization 방식
        def dp_memo(n):
            if n <= 1:
                memo[n] = 1
                return memo[n]

            if n in memo:
                return memo[n]

            memo[n] = dp_memo(n - 1) + dp_memo(n - 2)
            return memo[n]

        # Tabulation 방식이지만 따로 테이블을 생성하진 않는다
        def dp_tab(n):
            cur, prev = 1, 0
            for _ in range(n):
                cur, prev = cur + prev, cur
            return cur

        return dp_memo(n), dp_tab(n)

sol = Solution()
m, t = sol.climbStairs(40)
print(f'Memoization: {m}\nTabulation: {t}')