a = int(input())
b = int(input())
c = int(input())

output = a*b*c
outarr = [0,0,0,0,0,0,0,0,0,0]

while output > 1:
    i = int(output%10)
    outarr[i] = outarr[i]+1
    output = output/10

for i in outarr:
    print(i)
