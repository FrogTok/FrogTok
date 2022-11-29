# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def spin(key, m):
    new = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new[m - (j + 1)][i] = key[i][j]
    return new
            

def move(key, m, n, x, y):
    new_board = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            if(i + x >= 0 and i + x < n and j + y >= 0 and j + y < n):
                new_board[i + x][j + y] = key[i][j]
    return new_board

def is_correct(board, lock, n):
    for i in range(n):
        for j in range(n):
            if (board[i][j] ^ lock[i][j] == 0):
                return False
    return True
                
def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
    for _ in range(4):
        for i in range(-m + 1, m + n - 1):
            for j in range(-m + 1, m + n - 1):
                if(is_correct(move(key, m, n, i, j), lock, n)):
                    return True
        key = spin(key, m)
        
            
    
    return answer