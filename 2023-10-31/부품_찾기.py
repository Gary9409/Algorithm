# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
#
# N = 5
# [8, 3, 7, 9, 2]
# M = 3
# [5, 7, 9]

import sys

N = sys.stdin.readline()
l1 = set(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
l2 = list(map(int, sys.stdin.readline().split()))

print(*['yes' if x in l1 else 'no' for x in l2])

# 앞의 Intersection_of_Two_Arrays 문제와 동일하게 풀 수 있다.
# 다만 합집합을 반환하던 위 문제와는 달리 한 리스트를 돌며 합집합에 포함되는 요소를 T/F로 표현하도록 수정하면 된다.