# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    
    # P를 기준으로 2칸까지 모든 경로 탐색
    def dfs(x, y, dist):
        nonlocal visited
        nonlocal valid
        
        if (x, y) in visited or dist > 2 or place[x][y] == 'X':
            return
        
        # 해당 경로에 P가 있으면 valid를 0으로 수정
        if dist > 0 and place[x][y] == 'P':
            valid = 0
            return
        
        visited.add((x, y))
        
        if x > 0:
            dfs(x - 1, y, dist + 1)
        if x < 4:
            dfs(x + 1, y, dist + 1)
        if y > 0:
            dfs(x, y - 1, dist + 1)
        if y < 4:
            dfs(x, y + 1, dist + 1)
    
    # places를 순회하며 탐색
    for place in places:
        valid = 1
        visited = set()
        
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    dfs(x, y, 0)
        
        # 거리두기가 지켜졌으면 valid = 1, 아니면 valid = 0
        answer.append(valid)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# result = [1, 0, 1, 1, 1]
print(f'#1\nplaces = {places}\nresult = {solution(places)}')