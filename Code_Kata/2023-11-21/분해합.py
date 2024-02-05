import sys

input = sys.stdin.readline
n = int(input())

def min_generator(n):
    tmp = 1
    while tmp <= n:
        if tmp + sum(map(int, str(tmp))) == n:
            return tmp
        tmp += 1
    return 0

print(min_generator(n))