string = input().upper()
alphabet = [0]*26 #알파벳 대문자 수만큼 배열을 할당

for i in range(65, 91):
    alphabet[i-65] = string.count(chr(i))

if(alphabet.count(max(alphabet)) > 1):
    print("?")#예외처리
else:
    print(chr(alphabet.index(max(alphabet))+65))
