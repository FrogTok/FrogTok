n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

max = 0

for i in range(len(data)):
    data[i].sort()
    if (data[i][0] > max):
        max = data[i][0]

print(max)