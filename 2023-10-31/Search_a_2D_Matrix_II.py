# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List

class Solution:
    # 오른쪽 위에 포인터를 잡고 타겟보다 작으면 아래로, 타겟보다 크면 왼쪽으로 이동
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

    # any() 이용
    def searchMatrix_pythonic(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

sol = Solution()
mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
t1, t2 = 5, 20
print(sol.searchMatrix(mat, t1))
print(sol.searchMatrix_pythonic(mat, t1))
print(sol.searchMatrix(mat, t2))
print(sol.searchMatrix_pythonic(mat, t2))