# 연속해서 array의 요소를 선택할 수 없을 때,
# 선택한 요소합의 최댓값을 출력하시오.

# 입력 예제
# 4
# 1 3 1 5
# 출력 예제
# 8

n = int(input())
d = [0] * n

array = list(map(int, input().split()))

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])