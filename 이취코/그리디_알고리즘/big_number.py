data = []
result = 0
i = 0
count = 0

size, m, limit = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
data.reverse()

for _ in range(m):
    result += data[i]
    count += 1
    if (i > 0):
        i -= 1
    if (count == limit):
        count = 0
        i+=1
    
    if (i >= size):
        break

    m -= 1

print(result)

######## 수열을 구해서 푸는 법 ########

# n m k를 공백으로 구분하여 입력받기
n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = count * first # 가장 큰 수 더하기
result +=  (m - count) * second # 두 번째로 큰 수 더하기

print(result)