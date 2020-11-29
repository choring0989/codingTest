n = int(input())
m = list(map(int, input().split()))

n = 0

for i in m:
    f = 1
    for j in range(2, i-1):
        if(i!=j and i%j==0):
            f = 0
    if(i!=1 and f==1):
        n += 1

print(n)
