# https://www.acmicpc.net/problem/2437
n = int(input())

coins = list(map(int, input().split()))

coins.sort()

target = 1
for coin in coins:
    if (coin <= target):
        target += coin
    else:
        break

print(target)

