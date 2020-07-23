nonself = set()

def isNonSelf(n):
    num = 0
    if n < 10:
        num = n+n
    elif n < 100:
        num = n+(n//10)+(n%10)
    elif n < 1000:
        num = n+(n//100)+(n%100//10)+(n%100%10)
    elif n < 10000:
        num = n+(n//1000)+(n%1000//100)+(n%1000%100//10)+(n%1000%100%10)

    if num < 10001:
        nonself.add(num)

for l in range(1, 10001):
    isNonSelf(l)

for l in range(1, 10001):
    if l not in nonself:
        print(l)
    
