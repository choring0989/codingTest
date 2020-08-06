'''
#이렇게 짜면 안 돼요
def solution(mylist):
    answer = list()
    for j in mylist:
        answer.append(len(j))
    return answer
'''
def solution(mylist):
    return list(map(len, mylist))
