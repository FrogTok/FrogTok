h, w = map(int,input().split())
matrix = [[0] * w for _ in range(h)]
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if (d == 0):
        for i in range(y, y + l):
            matrix[x][i] = 1
    else:
        for i in range(x, x + l):
            matrix[i][y] = 1

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end = ' ')
    print()