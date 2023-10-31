# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List
from structure import BinarySearch

class Solution:
    def __init__(self):
        self.bs = BinarySearch()

    # 파이썬 내장함수 intersection() 이용
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    # my_binary_sort로 구현
    def my_intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        ret = set()
        for n in nums1:
            idx = self.bs.my_binary_search(nums2, n, 0, len(nums2) - 1)
            if idx < len(nums2) and nums2[idx] == n:
                ret.add(n)
        return list(ret)

sol = Solution()
n1, n2 = [1, 2, 2, 1], [2, 2]
print(sol.my_intersection(n1, n2))
n3, n4 = [4, 9, 5], [9, 4, 9, 8, 4]
print(sol.my_intersection(n3, n4))