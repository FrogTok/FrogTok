result = sum([1, 2, 4, 6, 8])
print(result)

result = min([1, 2, 3, 4, 5, 6, 7])
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 6, 5, 4], reverse = True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], reverse = True, key = lambda x:x[1])
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(data)

