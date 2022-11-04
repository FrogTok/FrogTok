n = int(input())
matrix = [[0] * 19 for _ in range(19)]

for _ in range(n):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(matrix[i][j], end = ' ')
    print()
