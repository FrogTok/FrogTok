# https://www.acmicpc.net/problem/18406
n = input()

mid = int(len(n) / 2)
sum_left = 0
sum_right = 0
for i in range(mid):
    sum_left += int(n[i])
    sum_right += int(n[i + mid])

if(sum_left == sum_right):
    print("LUCKY")
else:
    print("READY")