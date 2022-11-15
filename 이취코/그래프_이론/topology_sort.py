from collections import deque

v, e = map(int, input().split())

lines = [[] for _ in range(v + 1)]
degree = [0] * (v + 1)
q = deque()

for _ in range(e):
    n1, n2 = map(int, input().split())
    lines[n1].append(n2)
    degree[n2] += 1

for i in range(1, v + 1):
    if (degree[i] == 0):
        q.append(i)

result = []

while q:
    i = q.popleft()
    result.append(i)
    
    for node in lines[i]:
        degree[node] -= 1
        if (degree[node] == 0):
            q.append(node)
    

for i in result:
    print(i, end = ' ')