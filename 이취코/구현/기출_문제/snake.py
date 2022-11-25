# https://www.acmicpc.net/problem/3190

from collections import deque

directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우, 하, 좌, 상

n = int(input()) # 보드 사이즈
board = [[0] * n for _ in range(n)] # 빈공간: 0, 사과: 1, 뱀: 2 ~ ?

k = int(input()) # 사과 갯수
apple = [tuple(map(int, input().split())) for _ in range(k)] # 사과 좌표
for pos in apple:
    x = pos[0] - 1
    y = pos[1] - 1
    if(x < n and x >= 0 and y < n and y >= 0):
        board[x][y] = 1

l = int(input()) # 방향 변환 횟수
turns = deque() # 이동 칸수와 어디로 방향 꺾을지 (이동 칸수, 방향) L: 왼쪽 90도, D: 오른쪽 90도
for _ in range(l):
    a, b = input().split()
    turns.append((int(a), b))

time = 1 # 진행 시간

head = [0, 0] # 뱀의 머리 좌표
direct = 0 # 뱀의 머리 방향

tail = [0, 0] # 뱀의 꼬리 좌표

board[head[0]][head[1]] = 2 # 시작 지점 표시 2 부터 진행방향으로 증가

while True:
    nHead = [x + y for x, y in zip(head, directions[direct])]

    # 보드 넘어가면 실패
    if(nHead[0] < 0 or nHead[0] >= n or nHead[1] < 0 or nHead[1] >= n):
        break

    # 내몸에 부딧치면 실패
    if(board[nHead[0]][nHead[1]] >= 2):
        break

    # 다음 위치에 사과가 있는가?
    is_apple = True if board[nHead[0]][nHead[1]] == 1 else False

    # 전진
    board[nHead[0]][nHead[1]] = board[head[0]][head[1]] + 1
    head = nHead

    # 꼬리 지우기
    if (not is_apple):
        for i in range(4):
            nTail = [x + y for x, y in zip(tail, directions[i])]
            if(nTail[0] < 0 or nTail[0] >= n or nTail[1] < 0 or nTail[1] >= n):
                continue
            if (board[tail[0]][tail[1]] + 1 == board[nTail[0]][nTail[1]]):
                board[tail[0]][tail[1]] = 0
                tail = nTail
                break

    # 방향 정하기
    if(len(turns) != 0 and turns[0][0] == time):
        turn = turns.popleft()[1]
        if (turn == 'D'):
            direct = (direct + 1) % 4
        if (turn == 'L'):
            direct = (direct - 1) % 4
    time += 1

    print(time)
    for i in range(n):
        for j in range(n):
            print(board[i][j] % 8 + 2 if board[i][j] > 1 else board[i][j], end = ' ')
        print()
    print()

print(time)