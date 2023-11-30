import sys

n, k = map(int, sys.stdin.readline().split())
bag = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
table = [[0 for _ in range(len(bag))] for _ in range(k + 1)]

def max_val(k, bag):
    # 배낭의 최대무게를 1부터 k까지 늘려가면서 테이블을 갱신한다.
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            w, v = bag[j][0], bag[j][1]

            # 지금 보고있는 물건이 배낭용량보다 무겁다면, 이전 아이템까지의 최대값을 그대로 가져옴
            if i < w:
                table[i][j] = table[i][j - 1]

            # 배낭용량보다 가볍다면, 이 아이템을 배낭에 넣을 수 있는 상태의 배낭용량으로 돌아가 그 상태에서 물건을 배낭에 넣은 값과(table[배낭용량 - 아이템무게][이전 아이템] + 현재 아이템의 가치),
            # 이전 아이템까지의 최대값을 비교함(table[배낭용량][이전 아이템])
            else:
                table[i][j] = max(table[i][j - 1], table[i - w][j - 1] + v)

max_val(k, bag)
print(max(table[-1]))