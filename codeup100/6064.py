n1, n2, n3 = map(int, input().split())
res1 = n1 if (n1 < n2) else n2
print(res1 if (res1 < n3) else n3)