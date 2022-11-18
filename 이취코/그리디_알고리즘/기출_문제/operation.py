num = input()

result = int(num[0])
for i in range(1, len(num)):
    x = int(num[i])
    if (x <= 1 or result <= 1):
        result += x
    else:
        result *= x

print(result)