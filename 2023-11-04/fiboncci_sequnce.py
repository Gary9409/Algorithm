from time import time


# 일반적인 재귀함수으로 연산시 매개변수가 조금만 커져도 오래 걸린다
def fibo_recur(target):
    if target <= 1:
        return target
    return fibo_recur(target - 1) + fibo_recur(target - 2)

# 피보나치 수열의 결과값을 저장할 배열
fibo_memo = [None] * 41

# 메모이제이션을 활용한 다이나믹 프로그래밍으로 계산하면 빠르다
def fibo_dp(target):
    if target <= 1:
        fibo_memo[target] = target
        return fibo_memo[target]

    if fibo_memo[target]:
        return fibo_memo[target]

    fibo_memo[target] = fibo_dp(target - 1) + fibo_dp(target - 2)
    return fibo_memo[target]

start = time()
print(fibo_recur(40))
end = time()
print(f'Recursive: {end - start} sec')
start = time()
print(fibo_dp(40))
end = time()
print(f'Dynamic Programming: {end - start} sec')