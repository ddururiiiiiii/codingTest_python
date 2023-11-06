# n의 배수 고르기
def solution(n, numlist):
    answer = []

    for i in numlist:
        if i % n == 0:
            answer.append(i)

    return answer

# 자릿수 더하기
def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer

# OX퀴즈
def solution(quiz):
    answer = []

    for i in quiz:
        left, right = i.split(" = ")
        if eval(left) == int(right):
            answer.append("O")
        else :
            answer.append("X")

    return answer

# 숫자 찾기
def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1