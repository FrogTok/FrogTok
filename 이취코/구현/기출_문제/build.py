def possible(answer):    
        for structure in answer:
            x, y, a = structure
            # 기둥일 경우 놓을 수 있는지 체크
            # 바닥위거나, 보의 한쪽 끝이거나, 다른 기둥 위
            if(a == 0 and not (y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer)):
                return False
                
            # 보일 경우 놓을 수 있는지 체크
            # 한쪽 끝부분이 기둥 위거나, 양쪽 끝이 다른 보에 연결
            if(a == 1 and not ([x + 1, y - 1, 0] in answer or [x, y - 1, 0] in answer or ([x + 1, y, 1] in answer and [x - 1, y, 1] in answer))):
                return False
            
        return True
            
        
def solution(n, build_frame):
    answer = []
    
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        
        # 0이면 삭제, 1이면 넣기
        if(b == 0):
            answer.remove([x, y, a])
            print(x, y, a, b)
            if(not possible(answer)):
                answer.append([x, y, a])
        elif(b == 1):
            answer.append([x, y, a])
            if(not possible(answer)):
                answer.remove([x, y, a])
        
    # 최종 결과물 저장
    answer.sort()
    return answer


# 처음 짠 코드, 경우의 수 따지기가 너무 힘든구조였음
# 보 랑 기둥 좌표 겹칠때 구현할라다가 빡쳐서 다지움

# import copy

# def is_correct(wall, x, y, a):    
#         # 빈걸 유효성 체크하면 무조건 참
#         if(a == 0):
#             return True

#         px = x       # 기둥 위치 x좌표
#         py = y - 1   # 기둥 위치 y좌표
#         rpx = x + 1  # 오른쪽 기둥 위치 x좌표
#         rpy = y - 1  # 오른쪽 기둥 위치 x좌표
#         lbx = x - 1  # 왼쪽 보 위치 x좌표
#         lby = y      # 왼쪽 보 위치 y좌표
#         rbx = x + 1  # 오른쪽 보 위치 x좌표
#         rby = y      # 오른쪽 보 위치 y좌표
        
#         # 기둥일 경우
#         # 바닥위거나, 보의 한쪽 끝이거나, 다른 기둥 위
#         if(a == 1):
#             if(y == 0 or (lbx >= 0 and wall[lby][lbx] == 2) or (py >= 0 and wall[py][px] == 1)):
#                 return True
        
#         # 보일 경우
#         # 한쪽 끝부분이 기둥 위거나, 양쪽 끝이 다른 보에 연결
#         if(a == 2):
#             if((py >= 0 and wall[py][px] == 1) or (rpx < len(wall) and rpy >= 0 and (wall[rpy][rpx] == 1)) or((lbx >= 0 and wall[lby][lbx] == 2) and (rbx < len(wall) and wall[rby][rbx] == 2))):
#                 return True
    
        
#         return False
            
        
# def solution(n, build_frame):
#     answer = []
    
#     wall = [[0] * (n + 1) for _ in range(n + 1)] # 0: 빔, 1: 기둥, 2: 보
    
#     for i in range(len(build_frame)):
#         nWall = copy.deepcopy(wall) 
#         x, y, a, b = build_frame[i]
        
#         # 삽입인데 겹치면 무시
#         if(b == 1 and nWall[y][x] != 0):
#             continue
        
#         # 0이면 삭제, 1이면 넣기
#         if(b == 0):
#             nWall[y][x] = 0

#             # 아래는 체크할 필요 없으므로, 삭제후 좌우위만 체크
#             if((x - 1 < 0 or is_correct(nWall, x - 1, y, nWall[y][x - 1])) 
#                and (x + 1 >= n or is_correct(nWall, x + 1, y, nWall[y][x + 1])) 
#                and (y + 1 >= n or is_correct(nWall, x, y + 1, nWall[y + 1][x]))):
#                 wall = copy.deepcopy(nWall)
#         elif(b == 1):
#             nWall[y][x] = a + 1

#             # 구조물을 넣어도 규칙에 맞으면, wall에 반영
#             if(is_correct(nWall, x, y, a + 1)):
#                 wall = copy.deepcopy(nWall)
    
        
#     # 최종 결과물 저장
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if(wall[i][j] != 0):
#                 answer.append([j, i, wall[i][j] - 1])
#     answer.sort()
#     return answer