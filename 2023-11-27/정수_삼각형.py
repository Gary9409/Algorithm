import sys

tri = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

def dp(tri):
    for i in range(1, len(tri)):
        l = len(tri[i])
        tri[i][0] += tri[i - 1][0]
        tri[i][l - 1] += tri[i - 1][l - 2]
        for j in range(1, l - 1):
            tri[i][j] = max(tri[i][j] + tri[i - 1][j], tri[i][j] + tri[i - 1][j - 1])

    return max(tri[-1])

print(dp(tri))