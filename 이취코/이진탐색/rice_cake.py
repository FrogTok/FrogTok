# m의 길이만큼 떡을 주려고한다.
# 떡을 얼마의 길이로 잘라야 최소한으로 잘라서 주는 것이 되는가?

# 입력 예시
# 4 6
# 18 15 10 17

# 출력 예시
# 15

import sys

n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for x in array:
        if (x > mid):
            sum += x - mid
    if (sum < m):
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)