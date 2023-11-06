# 대문자로 바꾸기
def solution(myString):
    answer = myString.upper()
    return answer

# 소문자로 바꾸기
def solution(myString):
    answer = myString.lower()
    return answer

# A 강조하기
def solution(myString):
    answer = ''

    for i in myString:
        if i == 'a':
            answer += i.upper()
        elif i != 'A':
            answer += i.lower()
        else :
            answer += i


    return answer

# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    answer = []

    for i, v in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = v.lower()
        else :
            strArr[i] = v.upper()


    return strArr

# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    answer = ''

    for i in my_string:
        if i.lower() == alp.lower():
            answer += alp.upper()
        else :
            answer += i

    return answer