# https://school.programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd

def solution(w,h):
    return w * h - (w / gcd(w, h) + h / gcd(w, h) - 1) * gcd(w, h)

# 서로소인 w, h(w >= h)를 가지는 사각형에 대각선을 그으면, h개의 n*(w/h) 지점마다 대각선이 아랫줄로 내려오게 되고, 이 때마다 대각선이 그어지는 사각형이 한 개 씩 더 생기게 된다.
# 단, 대각선이 정확히 교점을 지나는 마지막 칸은 한 개의 사각형만 생기므로 최종적으로 h개에서 한 개를 뺀 갯수가 대각선이 지나가는 사각형의 갯수가 된다.
# 따라서, 대각선이 지나가는 사각형의 갯수는 w + h - 1개가 된다.
# 문제의 경우 w와 h가 서로소라는 조건이 없으므로 두 수의 최대공약수로 나눠 서로소로 만든 후 칸을 계산하고 최종적으로 나눠준 최대공약수만큼 곱한다.


w, h = 8, 12
# result = 80
print(f'#1\nw, h = {w}, {h}\nresult = {solution(w, h)}')