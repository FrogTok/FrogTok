# 10-8 도시 분할 계획
# 도시를 둘로 나눌 때, 총 도로 유지비가 최소가 되도록 하시오

# 입력 예시
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
# 출력 예시
# 8

import sys
import heapq

def find_root(parents, a):
    if (parents[a] != a):
        parents[a] = find_root(parents, parents[a])
    
    return parents[a]

def union(parents, a, b):
    root_a = find_root(parents, a)
    root_b = find_root(parents, b)

    if (root_a < root_b):
        parents[root_b] = root_a
        return root_b
    else:
        parents[root_a] = root_b
        return root_a

input = sys.stdin.readline

n, m = map(int, input().split())

q = []
parents = [i for i in range(n + 1)]
costs = [0] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(q, (cost, a, b))

while q:
    c, a, b = heapq.heappop(q)
    
    if (find_root(parents, a) == find_root(parents, b)):
        continue
    
    result = union(parents, a, b)
    costs[result] = c

print(sum(costs) - max(costs))