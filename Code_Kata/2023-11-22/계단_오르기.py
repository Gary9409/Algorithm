import sys

stairs = []
for _ in range(int(sys.stdin.readline())):
    stairs.append(int(sys.stdin.readline()))

memo = [None] * len(stairs)
def climb(n):
    if n == 0:
        memo[0] = stairs[0]
        return memo[0]
    if n == 1:
        memo[1] = max(stairs[0] + stairs[1], stairs[1])
        return memo[1]
    if n == 2:
        memo[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        return memo[2]

    if memo[n]:
        return memo[n]

    memo[n] = max(climb(n - 3) + stairs[n - 1] + stairs[n], climb(n - 2) + stairs[n])
    return memo[n]

print(climb(len(stairs) - 1))