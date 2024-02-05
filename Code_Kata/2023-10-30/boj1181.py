import sys

words = set()
for _ in range(int(sys.stdin.readline())):
    words.add(sys.stdin.readline().strip())
print(*sorted(words, key=lambda x: (len(x), x)), sep='\n')