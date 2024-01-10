# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    matrix = [[i for i in range(j * columns + 1, j * columns + columns + 1)] for j in range(rows)]

	# query에 따라 행렬을 회전시키는 함수
    def rotate(query):
        nonlocal matrix
        seq = []
        dx, dy = query[2] - query[0], query[3] - query[1]
        x, y = query[0] - 1, query[1] - 1
        ret = 10000
        
		# seq에 회전시킬 테두리의 좌표를 회전 역방향으로 넣는다.
        for _ in range(dx):
            seq.append((x, y))
            x += 1
        for _ in range(dy):
            seq.append((x, y))
            y += 1
        for _ in range(dx):
            seq.append((x, y))
            x -= 1
        for _ in range(dy):
            seq.append((x, y))
            y -= 1
        
		# 값이 계속 덮어씌워지므로 최초 시작값을 저장한다.
        tmp = matrix[x][y]
        
		# seq를 따라가며 해당 좌표를 그 다음 좌표의 값으로 덮어씌우며 최소값을 ret에 갱신한다.
        for i in range(len(seq) - 1):
            x, y = seq[i]
            nx, ny = seq[i + 1]
            ret = min(ret, matrix[x][y])
            matrix[x][y] = matrix[nx][ny]
        
		# 가장 마지막 좌표는 저장해두었던 값으로 처리한다.
        x, y = seq[-1]
        ret = min(ret, matrix[x][y])
        matrix[x][y] = tmp
        
		# 최소값을 반환한다.
        return ret
    
    for query in queries:
        answer.append(rotate(query))
    
    return answer


rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# result = [8, 10, 25]
print(f'#1\nrows, columns = {rows}, {columns}\nqueries = {queries}\nresult = {solution(rows, columns, queries)}\n')

rows, columns, queries = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# result = [1, 1, 5, 3]
print(f'#2\nrows, columns = {rows}, {columns}\nqueries = {queries}\nresult = {solution(rows, columns, queries)}\n')

rows, columns, queries = 100, 97, [[1,1,100,97]]
# result = [1]
print(f'#3\nrows, columns = {rows}, {columns}\nqueries = {queries}\nresult = {solution(rows, columns, queries)}')