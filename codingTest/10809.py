string = input()

for i in range(97, 123):
    print(string.find(chr(i)), end=" ")
    #find와 index가 있는데 index는 찾는 문자열이 없을 경우 오류 반환
    
