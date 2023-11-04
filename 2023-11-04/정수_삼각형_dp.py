import sys


input = sys.stdin.readline
tri = []
n = int(input())
for _ in range(n):
    tri.append(list(map(int, input().strip().split())))

# 경로의 합을 넣어줄 배열 생성
memo = [[int(1e9)] * n for n in range(1, n + 1)]
memo[0][0] = tri[0][0]
def dp(row, col):
    if not (0 <= row < n and 0 <= col < len(tri[row])):
        return 0

    if memo[row][col] != int(1e9):
        return memo[row][col]

    # 메모 배열의 해당 위치에 경로로 이을 수 있는 두 후보 중 큰 값을 더해준다
    memo[row][col] = tri[row][col] + max(dp(row - 1, col - 1), dp(row - 1, col))
    return memo[row][col]

# 배열을 순회하며 메모 배열을 채워나간다
for col in range(n):
    dp(n - 1, col)
print(max(memo[n - 1]))