# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 퀵 정렬을 구현
        def quick_sort(lst, start, end):
            def partition(part, ps, pe):
                i = ps - 1
                for j in range(ps, pe):
                    if part[j] <= part[pe]:
                        i += 1
                        part[i], part[j] = part[j], part[i]
                part[i + 1], part[pe] = part[pe], part[i + 1]
                return i + 1

            if start >= end:
                return None
            pivot = partition(lst, start, end)
            quick_sort(lst, start, pivot - 1)
            quick_sort(lst, pivot + 1, end)
            return lst

        # 병합 정렬을 구현
        def merge_sort(lst):
            def merge(lst1, lst2):
                res = []
                i = j = 0
                while i < len(lst1) and j < len(lst2):
                    if lst1[i] < lst2[j]:
                        res.append(lst1[i])
                        i += 1
                    else:
                        res.append(lst2[j])
                        j += 1
                if i < len(lst1):
                    res.extend(lst1[i:])
                if j < len(lst2):
                    res.extend(lst2[j:])
                return res

            if len(lst) <= 1:
                return lst
            left = lst[:len(lst) // 2]
            right = lst[len(lst) // 2:]
            return merge(merge_sort(left), merge_sort(right))

        # 전체 리스트를 한 번만 순회하고 정렬
        def one_pass(lst):

            # 배열의 양 끝과 중간을 가리키는 포인터를 잡아준다
            left, p, right = 0, 0, len(lst) - 1

            # p를 한 칸씩 이동시키며 0이 나오면 좌로, 2가 나오면 우로 보내주고 좌, 우의 포인터를 한 칸씩 안쪽으로 당겨준다
            while p <= right:
                if lst[p] == 0:
                    lst[p], lst[left] = lst[left], lst[p]
                    p += 1
                    left += 1
                elif lst[p] == 1:
                    p += 1
                else:
                    lst[p], lst[right] = lst[right], lst[p]
                    p += 1
                    right -= 1
            return lst

        # nums = quick_sort(nums, 0, len(nums) - 1)
        # nums = merge_sort(nums)
        nums = one_pass(nums)
        return nums

s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))