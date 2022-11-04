n = int(input())
n_list = list(map(int, input().split()))

min_num = n_list[0]
for i in range(n):
    if (n_list[i] < min_num):
        min_num = n_list[i]

print(min_num)