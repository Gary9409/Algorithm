# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    # a^2 + b^2 = d^2 에서 a값을 for문으로 순회하며 b값의 개수를 계산하여 더함
    return sum((int((d ** 2 - a ** 2) ** (1 / 2)) // k) + 1 for a in range(0, d + 1, k))


k, d = 2, 4
# result = 6
print(f'#1\nk, d = {k}, {d}\nresult = {solution(k, d)}\n')

k, d = 1, 5
# result = 26
print(f'#2\nk, d = {k}, {d}\nresult = {solution(k, d)}')