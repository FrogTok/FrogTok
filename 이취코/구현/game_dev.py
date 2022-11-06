# 캐릭터 움직임 메뉴얼
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다. 
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다. 

# 첫째줄에 N X M 맵의 세로 크기 N과 가로 크기 M을 입력 ( 3 <= N, M <= 50)
# 둘째줄 세 입력중 두번째까지는 좌표, 세번째는 바라보는 방향 (0 - 북, 1 - 동, 2 - 남, 3 - 서)
# 셋째줄부터 판때기 입력시 (0 - 육지, 1 - 바다)
# 방문한 칸수 출력

# 처음 서있는 위치의 상태는 무조건 육지이다
# 가본 칸은 9로 표시

n, m = map(int, input().split())
x, y, d = map (int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board[x][y] = 9
count = 1
turn_count = 0
while True:
    # 네방향 중 갈데 없으면 뒤로가기
    # 뒤로 못가면 탈출
    if (turn_count == 4):
        turn_count = 0
        nx = x - dx[d]
        ny = y - dy[d]
        if (board[nx][ny] == 0):
            x = nx
            y = ny
        else:
            break

    # 회전하기
    d -= 1
    if (d < 0):
        d = 3
    
    # 전진 할지 말지
    nx = x + dx[d]
    ny = y + dy[d]
    if ( ( nx >= 0 and ny >= 0 and nx < m and ny < m ) and board[nx][ny] == 0 ):
        x = nx
        y = ny
        board[x][y] = 9

        turn_count = 0
        count += 1
    else:
        turn_count += 1
    
for tiles in board:
    for tile in tiles:
        print(tile, end = ' ')
    print()
print(count)