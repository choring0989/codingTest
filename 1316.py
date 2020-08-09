'''
gword = 0

for i in range(int(input())):
    nowword = input()
    flag = 0
    for j in nowword:
        nowword = nowword.replace(j, "", 1)
        if(nowword.find(j) != -1 and nowword.find(j) != 0):
            flag += 1
    if(flag == 0):
        gword +=1

print(gword)
'''
result = 0

for i in range(int(input())):
    word = input()#소팅해보면 연속되지 않은 문자가 등장함을 알 수 있음
    if(list(word) == sorted(word, key=word.index)):
       result += 1

print(result)
    
