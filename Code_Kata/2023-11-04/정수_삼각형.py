import sys


input = sys.stdin.readline
tri = []
for _ in range(int(input())):
    tri.append(list(map(int, input().strip().split())))

# 기존 배열의 제일 위부터 아래까지 모두 순회하며 자신에게 연결될 수 있는 두 대각선 중 어떤 값이 큰 지를 확인하여 누적시킨다
def tabulation(tri):
    n = len(tri)

    for i in range(1, n):
        # 각 층의 양 끝은 후보가 하나이므로 따로 처리
        tri[i][0] += tri[i - 1][0]
        tri[i][i] += tri[i - 1][i - 1]
        # 남은 배열을 순회하며 둘 중 어느 값을 가져와서 더할지 결정
        for j in range(1, i):
            if tri[i - 1][j - 1] > tri[i - 1][j]:
                tri[i][j] += tri[i - 1][j - 1]
            else:
                tri[i][j] += tri[i - 1][j]

    return tri[n - 1]

print(max(tabulation(tri)))

# # 처음에는 테이블을 새로 만들어 값을 저장하였으나,
# # 모든 배열을 다 순회하는 상향식 탐색이므로 기존 배열을 수정하기만 해도 괜찮을 것 같아서 바꾸었다.
# def tabulation(tri):
#     n = len(tri)
#     tab.append(tri[0])
#
#     for i in range(1, n):
#         new = []
#         for j in range(i + 1):
#             if j == 0:
#                 new.append(tab[i - 1][j] + tri[i][j])
#             elif j == i:
#                 new.append(tab[i - 1][j - 1] + tri[i][j])
#             elif tab[i - 1][j - 1] > tab[i - 1][j]:
#                 new.append(tab[i - 1][j - 1] + tri[i][j])
#             else:
#                 new.append(tab[i - 1][j] + tri[i][j])
#         tab.append(new)
#
#     return tab[n - 1]
#
# print(max(tabulation(tri)))
