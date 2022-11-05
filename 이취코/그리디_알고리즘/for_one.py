num, d = map(int, input().split())

##### 한번에 빼는 방법 #####
result = 0
while num != 1:
    if (num % d == 0):
        num //= d
        result += 1
    else:
        count = num % d
        num -= count
        result += count
        
        if (num == 0):
            result -= 1
            break

print(result)

######## 1씩 빼는 방법#########
# result = 0

# while num != 1:
#     if (num % d == 0) :
#         num /= d
#     else:
#         num -= 1
#     result += 1

# print(result)