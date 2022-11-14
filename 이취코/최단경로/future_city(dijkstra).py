# 9-4 미래도시 문제, 다익스트라 알고리즘으로 풀이
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
import heapq
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

destination, waypoint =  map(int, input().split())

def dijkstra(start, end):
    if (start == end):
        return 0

    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    q = []

    distance[start] = 0
    visited[start] = True

    heapq.heappush(q, (0, start))

    while q:
        print(q)
        d, node = heapq.heappop(q)
        for next in graph[node]:
            if (not visited[next]):
                distance[next] = min(distance[next], d + 1)
                visited[next] = True
                heapq.heappush(q, (distance[next], next))
            
            if (next == end):
                q.clear()
                print("queue clear")
                break
                
    print(start, " to ", end, " = ", distance[end])
    return distance[end]


result = dijkstra(1, waypoint) + dijkstra(waypoint, destination)

if (result >= INF):
    print(-1)
else:
    print(result)