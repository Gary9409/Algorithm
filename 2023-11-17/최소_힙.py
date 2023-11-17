import heapq
import sys

input = sys.stdin.readline
def max_heap(cmd):
    heap = list()
    log = []
    for c in cmd:
        if c == 0 and len(heap) == 0:
            log.append(0)
        elif c == 0:
            n = heapq.heappop(heap)
            log.append(n)
        else:
            heapq.heappush(heap, c)

    return log

cmd = []
for _ in range(int(input())):
    cmd.append(int(input()))
print(*max_heap(cmd), sep='\n')