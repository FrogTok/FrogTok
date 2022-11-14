# 9-5 전보 보내기, 다익스트라 알고리즘
# start에서 전보를 보냈을 때, 전보를 받는 도시의 수와, 전부 받기까지 걸리는 시간을 출력

# 입력 예시
# 3 2 1
# 1 2 4
# 1 3 2
# 출력 예시
# 2 4

import heapq

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []

distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    d, node = heapq.heappop(q)

    if (distance[node] < d):
        continue
    
    for x in graph[node]:
        next, time = x
        cost = time + d
        if (cost < distance[next]):
            distance[next] = cost
            heapq.heappush(q, (distance[next], next))

num = 0
max_d = 0
for d in distance:
    if (d < INF):
        num += 1
        max_d = max(max_d, d)

print(num - 1, max_d)