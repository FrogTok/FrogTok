n = int(input())

for i in range(1, n + 1):
    one_p = i % 10
    if (one_p == 3 or one_p == 6 or one_p == 9):
        print("X", end = " ")
    else:
        print(i, end = " ")