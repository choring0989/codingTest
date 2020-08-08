def c():
    num = 0
    for i in range(1, int(input())+1):
        if i < 100:
            num += 1
            continue
        else:
            sub = set() #중복비허용
            crt = str(i)
            for n in range(1, len(crt)):
                sub.add(int(crt[n])-int(crt[n-1]))
            if len(sub) == 1:
                num += 1
    return num
    
print(c())
