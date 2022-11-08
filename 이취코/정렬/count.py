# 계수정렬
# 데이터가 100만이 넘지 않을 때 효과적이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = [0] * 10

for i in range(len(array)):
    result[array[i]] += 1

for i in range(len(result)):
    for _ in range(result[i]):
        print(i, end = ' ')

