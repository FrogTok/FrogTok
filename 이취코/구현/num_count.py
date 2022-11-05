n = int(input())

result = 0

######## 문자열로 다뤄서 해결 ########
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if ((str(i) + str(j) + str(k)).find('3') != -1):
                result += 1

######## 처음 푼 소스 #########
# for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             for time in [i, j, k]:
#                 ten_t = time // 10
#                 one_t = time % 10
#                 if (ten_t == 3 or one_t == 3):
#                     result += 1
#                     break
print(result)
            