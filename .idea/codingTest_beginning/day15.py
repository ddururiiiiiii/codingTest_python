# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer = []

    for i in arr:
        if i >= 50 and i % 2 == 0 :
            answer.append(i/2)
        elif i < 50 and i % 2 == 1:
            answer.append(i*2)
        else :
            answer.append(i)

    return answer

# 조건에 맞게 수열 변환하기 2
def solution(arr):
    idx = 0
    prev = arr

    while True:
        change = []
        for i in prev:
            if i >= 50 and i % 2 == 0: change.append(int(i / 2))
            elif i < 50 and i % 2 == 1: change.append(i * 2 + 1)
            else: change.append(i)

        same = all(a == b for a, b in zip(prev, change))
        if same:
            break
        idx += 1

        prev = change

    return idx

# 1로 만들기
def solution(num_list):
    answer = 0


    for i in num_list:
        while i != 1:
            if i % 2 == 0 : # 짝수
                i = i / 2
                answer += 1
            else :
                i = (i-1) / 2
                answer += 1

    return answer

# 길이에 따른 연산
def solution(num_list):
    if len(num_list) >= 11 :
        answer = 0
        for i in num_list: answer += i
    else :
        answer = 1
        for i in num_list:
            answer *= i

    return answer

#  원하는 문자열 찾기
def solution(myString, pat):
    answer = 0

    if pat.upper() in myString.upper() :
        answer = 1
    else : answer = 0

    return answer