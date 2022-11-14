# 9-4 미래도시 문제, 플로이드-워셜 알고리즘으로 풀이
# 입력예시1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 출력 예시1
# 3
# 입력예시2
# 4 2
# 1 3
# 2 4
# 3 4
# 출력 예시2
# -1

INF = int(1e9)

n, m = map(int, input().split())

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

destination, waypoint = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

result = distance[1][waypoint] + distance[waypoint][destination]

if (result >= INF):
    print(-1)
else:
    print(result)