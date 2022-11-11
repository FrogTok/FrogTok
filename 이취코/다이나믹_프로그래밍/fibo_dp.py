# 탑다운 기법 활용

d = [0] * 100

def fibo(n):
    if (n == 1 or n == 2):
        return 1
    
    if (d[n] != 0):
        return d[n]
    
    d[n] = fibo(n - 1) + fibo (n - 2)

    return d[n]

print(fibo(99))


# 바텀업 기법 활용

d = [0] * 100

d[1] = 1
d[2] = 1

goal = 99

for i in range(goal + 1):
    if (d[i] == 0):
        d[i] = d[i - 1] + d[i - 2]

print(fibo(99)) 