# 입력 예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from collections import deque

n = int(input())

parents = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
results = [0] * (n + 1)
times = [0] * (n + 1)
q = deque()

for i in range(1, n + 1):
    inputs = list(map(int, input().split()))
    
    times[i] = inputs[0]
    results[i] = times[i]

    j = 1
    while inputs[j] != -1:
        parents[inputs[j]].append(i)
        degree[i] += 1
        j += 1

for i in range(1, n + 1):
    if(degree[i] == 0):
        deque.append(q, i)

while q:
    i = deque.popleft(q)

    for parent in parents[i]:
        degree[parent] -= 1
        results[parent] = max(results[parent], results[i] + times[parent])
        
        if (degree[parent] == 0):
            deque.append(q, parent)


for result in results[1: n + 1]:
    print(result)