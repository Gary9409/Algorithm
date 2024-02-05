# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
from structure import BinarySearch

class Solution:
    def __init__(self):
        self.bs = BinarySearch()

    # binary search 이용
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            idx = self.bs.my_binary_search(numbers, target - numbers[i], i + 1, len(numbers) - 1)
            if idx < len(numbers) and numbers[idx] == target - numbers[i]:
                return [i + 1, idx + 1]

    # 배열이 정렬되어있음이 보장되므로 양 끝에 포인터를 잡고 안으로 좁히면서 찾을 수 있음
    def twoSum_pointers(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]

sol = Solution()
n1, t1 = [2, 7, 11, 15], 9
print(sol.twoSum_binary_search(n1, t1))
print(sol.twoSum_pointers(n1, t1))
n2, t2 = [2, 3, 4], 6
print(sol.twoSum_binary_search(n2, t2))
print(sol.twoSum_pointers(n2, t2))
n3, t3 = [-1, 0], -1
print(sol.twoSum_binary_search(n3, t3))
print(sol.twoSum_pointers(n3, t3))