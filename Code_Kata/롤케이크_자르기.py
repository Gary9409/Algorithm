# https://school.programmers.co.kr/learn/courses/30/lessons/132265

import collections

def solution(topping):
    answer = 0

    # Counter로 전체를 세서 오른쪽 롤케이크에 넣어준다
    l, r = set(), collections.Counter(topping)

    for i in topping:

        # 토핑 리스트를 돌며 왼쪽 토핑세트에 토핑을 추가하고, 오른쪽 Counter에서 하나씩 제거해준다
        l.add(i)
        r[i] -= 1

        # 오른쪽에 토핑이 다 떨어졌다면 딕셔너리에서 제거해준다
        if r[i] == 0:
            r.pop(i)

        # 세트와 딕셔너리의 길이를 비교해 왼쪽이 더 크면 더 이상 비교할 필요가 없으므로 종료
        if len(l) > len(r):
            break

        # 세트와 딕셔너리의 길이가 같으면 문제에서 원하는 커팅이므로 answer 증가
        if len(l) == len(r):
            answer += 1

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
# result = 2
print(f'#1\ntopping = {topping}\nresult = {solution(topping)}\n\n')

topping = [1, 2, 3, 1, 4]
# result = 0
print(f'#2\ntopping = {topping}\nresult = {solution(topping)}')