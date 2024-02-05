import sys
import collections

input = sys.stdin.readline

def circular_queue(seq, nums):
    deq = collections.deque(range(1, seq + 1))
    count = 0

    for n in nums:
        i = deq.index(n)
        if i <= len(deq) - i:
            count += i
            deq.rotate(-i)
            deq.popleft()
        else:
            count += len(deq) - i
            deq.rotate(len(deq) - i)
            deq.popleft()

    return count

seq, _ = map(int, input().split())
nums = list(map(int, input().split()))
print(circular_queue(seq, nums))