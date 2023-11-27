import sys

_ = sys.stdin.readline()
seq = list(map(int, sys.stdin.readline().split()))

def subseq(seq):
    sub = [1] * len(seq)

    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:
                sub[i] = sub[i] if sub[i] > sub[j] + 1 else sub[j] + 1

    return sub

print(max(subseq(seq)))