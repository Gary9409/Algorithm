n = int(input())
board = [None for _ in range(n)]

def isValid(row):
    for i in range(row):
        if board[row] == board[i]:
            return False
        if board[row] == board[i] + (row - i):
            return False
        if board[row] == board[i] - (row - i):
            return False

    return True

def nQueen(row, n, count):
    if row == n:
        count += 1
        return count

    for i in range(n):
        board[row] = i
        if isValid(row):
            count = nQueen(row + 1, n, count)

    return count

print(nQueen(0, n, 0))