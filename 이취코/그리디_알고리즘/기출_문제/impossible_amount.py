n = int(input())

coins = list(map(int, input().split()))

coins.sort()

target = 0
for coin in coins:
    if (coin <= target + 1):
        target += coin
    else:
        print(target + 1)
        break
