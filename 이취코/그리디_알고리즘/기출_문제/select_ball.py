n, m = map(int, input().split())

balls = list(map(int, input().split()))

# 처음 풀이
# result = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (balls[i] != balls[j]):
#             result += 1

# print(result)

# 그리디 적용
# A가 무게순으로 고르는 경우, B는 A가 고른 무게보다 높게 고른다.
# A가 고른 무게의 수 X B가 고르는 경우의 수

weights = [0] * 11
for ball in balls:
    weights[ball] += 1

result = 0
for i in range(1, m + 1):
    n -= weights[i] # A가 고른 무게 경우의 수 제외
    result += weights[i] * n # B가 고른 경우의 수 곱하기 

print(result)