matrix =[[] for _ in range(10)]

for i in range(10):
    matrix[i] = list(map(int, input().split()))

x = 1
y = 1

while True:
    if (matrix[x][y] == 0):
        matrix[x][y] = 9
    elif (matrix[x][y] == 2):
        matrix[x][y] = 9
        break

    if ((matrix[x + 1][y] == 1 and matrix[x][y + 1] == 1) or (x == 8 and y == 8)):
        break

    if (matrix[x][y + 1] != 1):
        y += 1
    elif (matrix[x + 1][y] != 1):
        x += 1

for i in range(10):
    for j in range(10):
        print(matrix[i][j], end = ' ')
    print()
    