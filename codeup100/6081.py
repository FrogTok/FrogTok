x = int(input(), 16)

i = 1
while i <= 0xF:
    print("%X*%X=%X"% (x, i, x*i))
    i += 1