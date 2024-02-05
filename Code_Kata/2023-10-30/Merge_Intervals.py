# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        # 숫자쌍을 정렬한 후 for문 순회
        for i, j in sorted(intervals):
            # 숫자쌍을 받아와서 res에 추가
            if len(res) == 0 or i > res[-1][1]:
                res.append([i, j])
            # 만약 새로 받은 숫자쌍의 시작점이 res의 마지막 숫자보다 작다면 그래프가 연결되어 있으므로 끝점의 값을 수정
            else:
                res[-1][1] = max(j, res[-1][1])
        return res

s = Solution()
print('Intervals: ')
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals)
print('Merged: ')
print(s.merge(intervals))