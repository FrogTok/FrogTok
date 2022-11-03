a, b, c = map(int, input().split())
sum = a + b + c
print(sum, "%.2f" % (sum / 3.0))

# 이건 2나 3으로 해도 소수점 첫째자리 까지만 출력됨.
#print(sum, round(sum / 3, 2))
