def hanoi(n, start, mid, end):
    if n <= 1:
        log = [f"{start} {end}"]
        return log

    return hanoi(n - 1, start, end, mid) + [f"{start} {end}"] + hanoi(n - 1, mid, start, end)

log = hanoi(int(input()), 1, 2, 3)
print(len(log))
print(*log, sep='\n')