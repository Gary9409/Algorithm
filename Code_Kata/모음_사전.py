# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer, stack = 0, ['U', 'O', 'I', 'E', 'A']

    # dfs방식으로 완전탐색
    while stack:
        # 몇 번째인지 체크하기 위해 매 탐색마다 answer 값을 하나씩 올려줌
        answer += 1
        cur = stack.pop()

        # 현재 단어가 목표단어이면 종료
        if cur == word:
            break
        # 현재 단어의 길이가 5이면 더 이상 자식노드를 추가하지 않음
        elif len(cur) == 5:
            continue

        # 현재 단어에서 모음을 하나 더 붙인 자식노드 5개 추가
        stack.extend([cur + vowel for vowel in "UOIEA"])

    return answer


word = "AAAAE"
# result = 6
print(f'#1\nword = {word}\nresult = {solution(word)}\n\n')

word = "AAAE"
# result = 10
print(f'#2\nword = {word}\nresult = {solution(word)}\n\n')

word = "I"
# result = 1563
print(f'#3\nword = {word}\nresult = {solution(word)}\n\n')

word = "EIO"
# result = 1189
print(f'#4\nword = {word}\nresult = {solution(word)}\n\n')