# 최단 경로 찾는 부분을 힙큐로 사용하여 O(ElogV)으로 최적화 한 알고리즘
# E는 간선의 갯수
# V는 노드의 갯수

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n + 1)
visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    visited[start] = True
    heapq.heappush(q, (0, start))

    while q:
        d, n = heapq.heappop(q)
        for i in graph[n]:
            if (not visited[i[0]] and d + i[1] < distance[i[0]]):
                distance[i[0]] = d + i[1]
                visited[i[0]] = True
                heapq.heappush(q, (d + i[1], i[0]))

dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])


                

