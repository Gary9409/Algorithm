# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 퀵 소팅으로 구현
        def quick_sort(s, start, end):
            def partition(part, ps, pe):
                i = ps - 1
                for j in range(ps, pe):
                    if part[j] < part[pe]:
                        i += 1
                        part[i], part[j] = part[j], part[i]
                part[i + 1], part[pe] = part[pe], part[i + 1]
                return i + 1

            if start >= end:
                return None

            p = partition(s, start, end)
            quick_sort(s, start, p - 1)
            quick_sort(s, p + 1, end)
            return s

        return quick_sort(list(s), 0, len(s) - 1) == quick_sort(list(t), 0, len(t) - 1)
        # # 파이썬 내장 함수를 이용하여 간단하게 소팅
        # return sorted(s) == sorted(t)

sol = Solution()
s, t = "anagram", "nagaram"
print(f'str1: {s}, str2: {t}')
print(sol.isAnagram("anagram", "nagaram"))