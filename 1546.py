leng = int(input())
input = list(map(int, input().split()))
max = max(input)
sum = 0

for i in range(leng):
    sum = sum + (input[i]/max*100)

print(sum/leng)

