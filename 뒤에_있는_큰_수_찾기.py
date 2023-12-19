# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):

    # 스택을 사용하여 풀이
    # 정답 배열 미리 길이만큼 생성
    answer, stack = [-1] * len(numbers), []

    for i in range(len(numbers)):

        # 스택에 쌓여있는 수들의 뒷큰수일 경우 정답 배열을 수정하면서 스택에서 제거
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    # 스택에 남아있는 인덱스들은 뒷큰수가 존재하지 않음
    while stack:
        answer[stack.pop()] = -1

    return answer


numbers = [2, 3, 3, 5]
# result = [3, 5, 5, -1]
print(f'#1\nnumbers = {numbers}\nresult = {solution(numbers)}\n\n')

numbers = [9, 1, 5, 3, 6, 2]
# result = [-1, 5, 6, 6, -1, -1]
print(f'#2\nnumbers = {numbers}\nresult = {solution(numbers)}')