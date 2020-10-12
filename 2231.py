n = int(input())
j = '1'
p = 0

while(int(j) <= n):
    k = int(j) + sum(list(map(int, j)))
    if(k == n):
        p = int(j)
        break
    j = str((int(j)+1))

print(p)
