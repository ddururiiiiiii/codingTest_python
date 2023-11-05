# 부분 문자열

def solution(str1, str2):
    answer = 0

    if str1 in str2: return 1
    else : return 0
    return answer


# 꼬리 문자열

def solution(str_list, ex):
    answer = ''

    for i in str_list:
        if ex not in i :
            answer += i
    return answer


# 정수 찾기

def solution(num_list, n):
    answer = 0

    for i in num_list:
        if n == i:
            return 1
    return answer
    # return int(n in num_list)


# 주사위 게임 1

def solution(a, b):
    answer = 0

    if a % 2 != 0 and b % 2 != 0:
        answer = (a ** 2) +  (b ** 2)
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)

    return answer


# 날짜 비교하기

from datetime import datetime
def solution(date1, date2):
    answer = 0

    date01 = datetime(date1[0], date1[1], date1[2])
    date02 = datetime(date2[0], date2[1], date2[2])

    if date01 < date02:
        return 1
    else : return 0
    return answer
    # int(date1 < date2)