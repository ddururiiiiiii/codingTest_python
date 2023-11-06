# 369게임
def solution(order):
    answer = 0

    for i in str(order):
        if i == "3" or i == "6" or i == "9":
            answer += 1

    return answer

# 암호해독
def solution(cipher, code):
    answer = ''

    for i in range(code, len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]

    return answer

# 대문자와 소문자
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

# 가까운 수
def solution(array, n):
    array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]