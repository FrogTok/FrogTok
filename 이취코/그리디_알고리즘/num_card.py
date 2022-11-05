n, m = map(int, input().split())
result = 0

for i in range(n):
   data = list(map(int, input().split()))
   min_value = min(data)
   result = max(result, min_value)

# 처음 작성한 코드
#data = [list(map(int, input().split())) for _ in range(n)]

#result = 0

#for i in range(n):
#    data[i].sort()
#    if (data[i][0] > result):
#        result = data[i][0]

print(result)