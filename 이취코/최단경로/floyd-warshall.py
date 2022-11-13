# 모든 노드에 대한 최단 경로를 2차원 배열로 저장한다.
# 각 노드를 순회 할 때 마다, a-> 노드, 노드 -> b 의 경우와 현재 최단 경로값을 비교하여 최솟값을 저장한다.

# 입력 예시
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
# 출력 예시
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0

INF = int(1e9)

n = int(input())
m = int(input())

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
           distance[j][k] =  min(distance[j][k] > distance[j][i] + distance[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (distance[i][j] == INF):
            print("INFINITY", end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print()