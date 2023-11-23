import sys

_ = sys.stdin.readline()
pList = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
print(sum(pList[i] * (i + 1) for i in range(len(pList))))