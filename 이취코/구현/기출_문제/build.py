def build_structure(wall, x, y, a):
        px = x      # 기둥 위치 x좌표
        py = y - 1  # 기둥 위치 y좌표
        lbx = x - 1  # 왼쪽 보 위치 x좌표
        lby = y      # 왼쪽 보 위치 y좌표
        rbx = x + 1  # 오른쪽 보 위치 x좌표
        rby = y      # 오른쪽 보 위치 y좌표
        
        # 아래에 기둥이 있거나, 양쪽에 보가 있거나, 바닥이면 설치하기
        if (y == 0 or (py >= 0 and wall[py][px] == 0) or (lbx >= 0 and wall[lby][lbx] == 1 and rbx < len(wall) and wall[rby][rbx] == 1)):
            wall[y][x] = a
            return True
        else:
            return False
        
def solution(n, build_frame):
    answer = []
    
    wall = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if(b == 0):
            wall[y][x] = 0
        elif(b == 1):
            result = build_structure(wall, x, y, a)
            if(result):
                answer.append([x, y, a])
    answer.sort() 
    return answer