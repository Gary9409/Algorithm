# https://medium.com/@rishidarkdevil/the-drunk-passenger-problem-554ebb7bd151

import random

# 문제를 직접 시뮬레이션하는 코드
class Solution:
    def __init__(self, passengers=100):
        self.passengers = passengers
        self.seats = set(range(passengers))

    def _choose_seat(self, ticket):
        if ticket == 0 or ticket not in self.seats:
            target = random.choice(list(self.seats))
            self.seats.discard(target)
        else:
            self.seats.discard(ticket)

    def board(self):
        for ticket in range(self.passengers - 1):
            self._choose_seat(ticket)
        return True if self.passengers - 1 in self.seats else False


# 실제 수행한 결과 50%에 근접하는 것을 확인 가능
for _ in range(10):
    res = [0, 0]
    for _ in range(10000):
        s = Solution()
        if s.board():
            res[0] += 1
        else:
            res[1] += 1
    print(res)