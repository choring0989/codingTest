a, b, v = map(int, input().split(" "))

if((v-b)%(a-b)==0):
    n = (v-b)//(a-b)
else:
    n = (v-b)//(a-b) + 1
print(n)
