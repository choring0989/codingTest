croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

for c in croa:
    string = string.replace(c, "T")#크로아티아 알파벳을 아무 문자열 하나로 변경

print(len(string))
