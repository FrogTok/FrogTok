n = int(input())
n_list = list(map(int, input().split()))

called = [0] * 23

for i in range(n):
    called[n_list[i] - 1] += 1

for i in range(23):
    print(called[i], end = ' ')