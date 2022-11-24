# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def compress(s, num):
    if(len(s) <= num):
        return len(s)
    
    comp = ""    
    length = len(s)
    
    count = 1
    word = s[0 : num]
    i = num
    
    while True:
        now = s[i : i + num] if i <= length else s[(i - num + length % num) : length]
        
        if(i > length or word != now):
            if (count > 1):
                comp += str(count)
            comp += word
            
            word = now
            count = 1
        else:
            count += 1
            
        if (i > length):
            break
        i += num
        
    return len(comp)
        
        
        
def solution(s):
    answer = len(s)
    for i in range(1, len(s) + 1):
        answer = min(answer, compress(s, i))
    
    return answer
