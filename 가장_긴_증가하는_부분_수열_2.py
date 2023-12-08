import bisect
import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

# LIS(Longest Increasing Subsequence) 사용하여 풀이
def subseq2(seq, n):
    # memo[i] == 만들 수 있는 i+1 길이의 부분수열 중 제일 작은 마지막값
    # 따라서 모든 seq를 순회하고 나면 memo의 길이가 최장길이가 된다
    memo = [seq[0]]

    for i in range(1, n):
        # seq를 돌며 memo에서 어느 위치에 넣을 수 있는지 체크 (l == index)
        l = bisect.bisect_left(memo, seq[i])
        # 만약 memo에 들어있는 모든 값보다 크다면 memo의 제일 뒤에 추가해 최장길이 부분수열의 길이를 늘림
        if l >= len(memo):
            memo.append(seq[i])
        # memo의 l번째에 들어가야 하는데, seq값을 비교해서 기존의 memo[l]보다 작을 때만 memo를 갱신
        # 작을 때 갱신해야 다음 들어오는 seq들에 대해서 제대로 비교가 가능
        elif memo[l] > seq[i]:
            memo[l] = seq[i]

    return memo

print(len(subseq2(seq, n)));