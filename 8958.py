num = int(input())

for i in range(num):
    flag = 1
    sum = 0
    q = input()
    for j in range(len(q)):
        if(q[j] == 'O'):
            sum = sum + flag
            flag += 1
        else:
            flag = 1
    print(sum)
