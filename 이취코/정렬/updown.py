n = int(input())

array = [int(input()) for _ in range(n)]

array.sort()
array.reverse()

for i in range(n):
    print(array[i], end = ' ')