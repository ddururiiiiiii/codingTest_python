# 커피 심부름
def solution(order):
    answer = 0

    for i in order:
        if "americano" in i:
            answer += 4500
        elif  "cafelatte" in i :
            answer += 5000
        else :
            answer += 4500

    return answer

# 그림 확대
def solution(picture, k):
    answer = []

    for i in picture:
        char = ""
        for j in i:
            char += j*k
        for a in range(k):
            answer.append(char)

    return answer

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []

    if k % 2 == 0:
        for i in arr:
            answer.append(i+k)
    else :
        for i in arr:
            answer.append(i*k)

    return answer

# l로 만들기
def solution(myString):
    answer = ''

    for i in myString:
        if ord(i) < ord("l"):
            answer += "l"
        else :
            answer += i

    return answer



# 특별한 이차원 배열 1
def solution(n):

    answer=[[0]*n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer