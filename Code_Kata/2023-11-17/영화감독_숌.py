import sys

input = sys.stdin.readline

count = 0
target = int(input())
num = 666
while True:
    if '666' in str(num):
        count += 1
        if count >= target:
            break
    num += 1
print(num)