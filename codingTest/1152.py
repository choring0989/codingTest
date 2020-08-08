### 1.슬라이딩윈도우
string = input()
count = 0

for i in range(1, len(string)):
    if string[i-1] != " " and string[i] == " ":
        count += 1
if (string[-1] == " "):
    print(count)
else:
    print(count+1)

### 2.내장함수 쓰기
string = input().split()
print(len(string))
