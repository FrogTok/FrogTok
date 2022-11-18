s = input()

# 처음에 나오는 수가 무조건 더 많거나 같다.
result = 0
for i in range(len(s)):
    if (s[i] == s[0]):
        continue
    
    # s[0] 와 다르니까 무조건 1부터 시작
    if ( s[i - 1] == s[0]):
        result += 1

print(result)