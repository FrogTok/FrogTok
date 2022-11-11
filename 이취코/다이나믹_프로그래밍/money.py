# 그리디를 사용하는 거스름돈 문제와 달리, 화폐 단위가 배수가 아니다.
# n개의 화폐로 m을 만들기 위한 최소한의 화폐 수를 출력.

# 입력 예시1
# 2 15
# 2
# 3
# 출력 예시1
# 5

# 입력 예시2
# 3 4
# 3
# 5
# 7
# 출력 예시2
# -1


n, m = map(int, input().split())

money = [int(input()) for _ in range(n)]

d = [-1] * 10001

for i in money:
    d[i] = 1

for i in range(1, m + 1):
    for x in money:
        if (i - x > 0 and d[i - x] != -1):
            if(d[i] != -1):
                d[i] = min(d[i], d[i - x] + 1)
            else:
                d[i] = d[i - x]


print(d[m])