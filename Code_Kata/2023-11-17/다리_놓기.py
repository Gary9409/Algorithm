import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n))))