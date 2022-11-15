# 10-5 크루스칼 알고리즘
# 최소 신장 트리가 될 때, 모든 간선의 합을 출력

# 입력 예시
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# 출력 예시
# 159

import heapq

def find_root(parents, node):
    if (parents[node] != node):
        parents[node] = find_root(parents, parents[node])
    return parents[node]

def union (parents, n1, n2):
    root_n1 = find_root(parents, n1)
    root_n2 = find_root(parents, n2)
    
    if (root_n1 == root_n2):
        return -1
    
    if (root_n1 < root_n2):
        parents[root_n2] = root_n1
        return root_n2
    else:
        parents[root_n1] = root_n2
        return root_n1


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
costs = [0 for _ in range(n + 1)]
q = []

for _ in range(m):
    n1, n2, c = map(int, input().split())
    heapq.heappush(q, (c, n1, n2))

while q:
    c, n1, n2 = heapq.heappop(q)
    
    result = union(parents, n1, n2)

    if (result != -1):
        costs[result] = c

sum = 0
for cost in costs:
    sum += cost

print(sum)

