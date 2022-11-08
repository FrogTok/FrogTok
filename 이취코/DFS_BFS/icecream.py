# 입력 예시
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, x, y):
    graph[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx >= 0 and ny >= 0 and nx < n and ny < m):
            if (graph[nx][ny] == 0):
                dfs(graph, nx, ny)
        

n, m = map(int, input().split())
matrix = [list(map(int,input())) for _ in range(n)] # 마지막에 띄어쓰기 있으면 오류나니 조심
result = 0

for i in range(n):
    for j in range(m):
        if (matrix[i][j] == 0):
            dfs(matrix, i, j)
            for k in range(n):
                for l in range(m):
                    print(matrix[k][l], end = ' ')
                print()
            print()
            result += 1

print(result)
