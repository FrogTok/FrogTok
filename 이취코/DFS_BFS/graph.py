#      0
#    1   2
# 0-1 비용 : 7
# 0-2 비용 : 5

# 인접행렬 방식
INF = 99999999

graph = [
    [0, 7, 5]
    [7, 0, INF]
    [5, INF, 0]
]

print(graph)

# 인접 리스트 방식

graph = [[] for _ in range(3)]

graph[0].append((1 ,7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)