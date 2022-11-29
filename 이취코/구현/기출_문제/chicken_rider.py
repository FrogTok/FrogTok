# https://www.acmicpc.net/problem/15686
from itertools import combinations

INF = int(1e9)

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

house = []
chiken = []

# house, chiken 배열에 각각 위치 좌표 저장
for i in range(n):
    for j in range(n):
        place = map[i][j] # 0: 도로, 1: 집, 2: 치킨집
        if (place == 1):
            house.append((i, j))
        elif (place == 2):
            chiken.append((i, j))

# 각 집에서 치킨거리의 합의 최솟값
min_sum = INF
# 치킨집 중, 폐업 안시킬곳 M개를 고른 모든 경우
for comb in list(combinations(chiken, m)):
    sum = 0
    # 각 집의 치킨거리 합 구하기
    for i in range(len(house)):
        chiken_dis = distance(house[i], comb[0])
        # 치킨집과 최소 거리 구하기
        for j in range(1, len(comb)):
            if(distance(house[i], comb[j]) < chiken_dis):
                chiken_dis = distance(house[i], comb[j])
        sum += chiken_dis
    # 치킨 거리 합의 최솟값 저장
    min_sum = min(min_sum, sum)

print(min_sum)
