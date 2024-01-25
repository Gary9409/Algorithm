# https://school.programmers.co.kr/learn/courses/30/lessons/135807

import math

def solution(arrayA, arrayB):
    gcdA, gcdB = arrayA[0], arrayB[0]
    
    # 각 배열의 최대공약수 구하기
    for a in arrayA[1:]:
        gcdA = math.gcd(gcdA, a)
    for b in arrayB[1:]:
        gcdB = math.gcd(gcdB, b)
    
    # 반대 배열에서 해당 최대공약수로 나눠지는 수 찾기
    # 최대공약수로 나눠지는 수는 그 최대공약수의 약수로도 나눠지기 때문에 최대공약수만 확인
    for b in arrayB:
        qout, mod = divmod(b, gcdA)
        if qout > 0 and mod == 0:
            gcdA = 0
            break
    for a in arrayA:
        qout, mod = divmod(a, gcdB)
        if qout > 0 and mod == 0:
            gcdB = 0
            break

    return max(gcdA, gcdB)


arrayA, arrayB = [10, 17], [5, 20]
# result = 0
print(f'#1\narrayA = {arrayA}\narrayB = {arrayB}\nresult = {solution(arrayA, arrayB)}\n')

arrayA, arrayB = [10, 20], [5, 17]
# result = 10
print(f'#2\narrayA = {arrayA}\narrayB = {arrayB}\nresult = {solution(arrayA, arrayB)}\n')

arrayA, arrayB = [14, 35, 119], [18, 30, 102]
# result = 7
print(f'#3\narrayA = {arrayA}\narrayB = {arrayB}\nresult = {solution(arrayA, arrayB)}')