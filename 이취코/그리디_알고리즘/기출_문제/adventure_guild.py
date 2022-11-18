# 입력 예시 1
# 20
# 1 2 2 3 3 3 4 4 4 5 5 5 5 5 6 6 6 6 6 6
# 출력 예시 1
# 5
# 입력 예시 2
# 27
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7
# 출력 예시 2
# 6
# 입력 예시 3
# 6
# 4 3 3 3 3 2
# 출력 예시 3
# 2

n = int(input())

fears = list(map(int, input().split()))

# 오름 차순
fears.sort()

result = 0
count = 0
for fear in fears:
    count += 1
    if (count >= fear):
        result += 1
        count = 0

print(result)

# 내림 차순
fears.sort(reverse = True)

result = 0
i = 0
while i < n:
    if (i + fears[i] <= n):
        result += 1
        i += fears[i]
    else:
        i += 1

print(result)