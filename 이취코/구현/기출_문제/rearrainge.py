s = input()

text = []
digit = 0

for c in s:
    if(c.isalpha()):
        text.append(c)
    else:
        digit += int(c)

text.sort()
text.append(str(digit))
print(text)