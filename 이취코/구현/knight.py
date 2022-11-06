st = input().upper()
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, -2, -2, 1, -1, 2, 2]
result = 0

x = int(ord(st[0])) - int(ord('A'))
y = int(st[0]) - 1

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if (nx < 0 or ny < 0 or nx > 7 or ny > 7):
        continue
    result += 1

print(result)
