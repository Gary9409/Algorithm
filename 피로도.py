# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = -1
    visited = []

    # dfs로 모든 던전을 돌면서 가능한 경우를 체크
    def dfs(k, ans):
        nonlocal answer

        for i, dungeon in enumerate(dungeons):
            # 현재 남은 피로도가 해당 던전의 최소피로도보다 크고, 해당 던전을 방문하지 않았으면 방문
            if k >= dungeon[0] and i not in visited:
                # 방문한 던전에 해당 던전의 인덱스 추가
                visited.append(i)
                # 피로도를 던전 요구치만큼 줄이고 방문 던전수를 1 추가
                dfs(k - dungeon[1], ans + 1)
                # 탐색이 끝났으므로 방문한 던전에서 제거
                visited.pop()

        # 가능한 모든 던전을 순회한 후 방문 던전수를 제일 큰 값으로 갱신
        answer = max(answer, ans)

    dfs(k, 0)

    return answer


k, dungeons = 80, [[80, 20], [50, 40], [30, 10]]
print(f'k = {k}')
print(f'dungeons = {dungeons}')
print(f'answer = {solution(k, dungeons)}')  # result = 3
