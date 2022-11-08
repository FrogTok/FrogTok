## 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(matrix, n, m):
    queue = deque()
    queue.append([0, 0, 1])

    while queue:
        x, y, move = queue.popleft()
        matrix[x][y] = 9

        if (x == n - 1 and y == m - 1):
            return move

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx >= 0 and ny >=0 and nx < n and ny < m):
                if (matrix[nx][ny] == 1):
                    queue.append((nx, ny, move + 1))
        



n, m = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(n)]

result = bfs(matrix, n, m)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()

print(result)
