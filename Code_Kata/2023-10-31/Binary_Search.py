# https://leetcode.com/problems/binary-search/
import bisect
from typing import List
from structure import BinarySearch
class Solution:
    def __init__(self):
        # 바이너리 서치 구현
        self.bs = BinarySearch()

    def search(self, nums: List[int], target: int) -> int:
        return self.bs.binary_search(lst, target, 0, len(nums) - 1)

    def my_search(self, nums: List[int], target: int) -> int:
        return self.bs.my_binary_search(nums, target, 0, len(nums) - 1)


sol = Solution()
lst, t1, t2 = [-1, 0, 3, 5, 9, 12], 9, 2
print(f'List: {lst}, Target: {t1}')
print(f'BinarySearch: {sol.search([-1, 0, 3, 5, 9, 12], 9)}')
print(f'myBinarySearch: {sol.my_search([-1, 0, 3, 5, 9, 12], 9)}')
print(f'List: {lst}, Target: {t2}')
print(f'BinarySearch: {sol.search([-1, 0, 3, 5, 9, 12], 2)}')
print(f'myBinarySearch: {sol.my_search([-1, 0, 3, 5, 9, 12], 2)}')