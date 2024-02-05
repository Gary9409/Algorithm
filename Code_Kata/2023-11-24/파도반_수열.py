def padovan_seq(n):
    if n < 2:
        return n

    p, q, cur = 0, 1, 1
    for _ in range(n - 2):
        p, q, cur = q, cur, p + q

    return cur

for _ in range(int(input())):
    print(padovan_seq(int(input())))