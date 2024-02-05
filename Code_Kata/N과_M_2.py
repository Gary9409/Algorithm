n, m = map(int, input().split())
seqs = []

def seq(n, m, sub):
    if len(sub) == m:
        print(*sub, sep=" ")
        return

    p = sub[-1] + 1 if sub else 1

    for i in range(p, n + 1):
        sub.append(i)
        seq(n, m, sub)
        sub.pop()

seq(n, m, [])