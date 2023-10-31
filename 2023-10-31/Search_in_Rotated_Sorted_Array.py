# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List
from structure import BinarySearch

class Solution:
    def __init__(self):
        self.bs = BinarySearch()
    def search(self, nums: List[int], target: int) -> int:
        # 가장 낮은 값의 인덱스를 찾는 메소드
        def min_idx(lst):
            # 좌, 우에 투 포인터
            left, right = 0, len(lst) - 1
            while left < right:
                # 중앙에 포인터
                p = left + (right - left) // 2
                # p의 값이 오른쪽보다 크면 앞 절반 제외
                if lst[p] > lst[right]:
                    left = p + 1
                # p의 값이 왼쪽보다 크면 뒤 절반 제외
                else:
                    right = p
            return left

        min = min_idx(nums)
        added = nums + nums[:min]
        ret = self.bs.my_binary_search(added, target, min, len(added) - 1)
        return ret if ret == -1 else ret % len(nums)

sol = Solution()
lst, lst2, t1, t2 = [4, 5, 6, 7, 0, 1, 2], [1], 0, 3
print(f'List: {lst}, Target: {t1}')
print(sol.search(lst, t1))
print(f'List: {lst}, Target: {t2}')
print(sol.search(lst, t2))
print(f'List: {lst2}, Target: {t1}')
print(sol.search(lst2, t1))