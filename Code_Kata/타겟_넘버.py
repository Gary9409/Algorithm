# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    def dfs(s, n):
        nonlocal answer

        # 배열을 다 돌았을 때, 합이 target이면 카운트 1 증가
        if n == len(numbers):
            if s == target:
                answer += 1
            return

        # 다음 숫자를 더할 때와 뺄 때로 나누어 dfs 진행
        dfs(s + numbers[n], n + 1)
        dfs(s - numbers[n], n + 1)

    dfs(0, 0)

    return answer


numbers, target = [1, 1, 1, 1, 1], 3
print('#1')
print(f'numbers = {numbers}')
print(f'target = {target}')
print(f'answer = {solution(numbers, target)}\n')

numbers, target = [4, 1, 2, 1], 4
print('#2')
print(f'numbers = {numbers}')
print(f'target = {target}')
print(f'answer = {solution(numbers, target)}')
