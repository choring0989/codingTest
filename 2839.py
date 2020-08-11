kg = int(input())
p = list() # 5kg백 사용이 가능한 양수의 경우를 넣을 것임

for i in range(0, kg):
    temp = (kg-(3*i))/5
    # 5kg 가능(방정식이 정수로 나눠떨어질때)이 temp, 5kg가 0번 들어가도 포함
    if temp.is_integer() and temp > -1:
        p.append(temp)# p에 5kg백이 필요한 갯수를 넣어둠

if(len(p) != 0):
    print(int((max(p))+((kg-(max(p)*5))//3)))# 5kg백 사용 수 + 3kg백 사용 
else:
    print(-1)
