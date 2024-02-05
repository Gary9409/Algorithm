import sys

input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

def div_and_conq(n, x, y):
    global blue, white
    count = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j]:
                count += 1
    if count == n * n:
        blue += 1
    elif count == 0:
        white += 1
    else:
        n //= 2
        div_and_conq(n, x, y)
        div_and_conq(n, x, y + n)
        div_and_conq(n, x + n, y)
        div_and_conq(n, x + n, y + n)

div_and_conq(n, 0, 0)
print(white, blue, sep="\n")