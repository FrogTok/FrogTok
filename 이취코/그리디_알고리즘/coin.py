n = int(input())
count = 0

coin = [500, 100, 50, 10]

for i in range(len(coin)):
    count += n // coin[i]
    n = n % coin[i]

print(count)