# 특정 문자 제거하기

def solution1(my_string, letter):
    answer = ''

    answer = my_string.replace(letter, "")

    return answer

# 각도기
def solution2(angle):
    answer = 0

    if angle < 90 :
        answer = 1
    elif angle == 90 :
        answer = 2
    elif angle > 90 :
        if angle < 180:
            answer = 3
        elif angle == 180:
            answer = 4

    return answer

# 양꼬치
def solution3(n, k):
    answer = 0

    if n >= 10:
        answer = n * 12000 + k * 2000
        service = (n // 10) *2000
        answer -= service
    else:
        answer = n * 12000 + k * 2000

    return answer

# 짝수의 합
def solution4(n):

    answer = 0

    for i in range(2, n+1, 2):
        if(i % 2 == 0):
            answer += i

    return answer