# x 사이의 개수
def solution(myString):
    answer = []
    arr = myString.split("x")

    for i in arr:
        answer.append(len(i))


    return answer


# 문자열 잘라서 정렬하기
def solution(myString):
    answer = []

    arr = [string for string in myString.split("x") if string]
    arr.sort()

    return arr

# 간단한 식 계산하기
def solution(binomial):
    answer = eval(binomial)
    return answer

# 문자열 바꿔서 찾기
def solution(myString, pat):
    answer = 0
    string = ""
    for i in myString:
        if i == "A" :
            string += "B"
        else :
            string += "A"

    if pat in string:
        return 1
    else : return 0

    return answer

# rny_string
def solution(rny_string):
    answer = rny_string.replace("m", "rn")
    return answer
 