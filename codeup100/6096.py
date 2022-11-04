matrix = [[] for _ in range(19)]

for i in range(19):
    matrix[i] = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(19):
        if(matrix[x][i] == 0):
            matrix[x][i] = 1
        else:
            matrix[x][i] = 0

        if(matrix[i][y] == 0):
            matrix[i][y] = 1
        else:
            matrix[i][y] = 0

for i in range(19):
    for j in range(19):
        print(matrix[i][j], end = ' ')
    print()