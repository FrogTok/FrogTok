n = int(input())
moves = list(input().split())

##### if 문을 줄인 코드 #####
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

x = 1
y = 1

for move in moves:
    for i in range(len(move_type)):
        if (move == move_type[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    
    if (nx < 1 or ny < 1 or nx > n or ny > n):
        continue

    x, y = nx, ny

#### 처음 작성한 코드 #####
# x = 1
# y = 1
# for i in range(len(move)):
#     if (move[i] == 'R' and y + 1< n + 1):
#         y += 1
#     elif (move[i] == 'L' and y - 1 > 0):
#         y -= 1
#     elif (move[i] == 'U' and x - 1 > 0):
#         x -= 1
#     elif (move[i] == 'D' and x + 1 < n + 1):
#         x += 1

print (x, y)