# 옷가게 할인 받기
def solution1(price):
    answer = 0

    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95

    return int(answer)

# 아이스 아메리카노
def solution2(money):
    answer = []

    result1 = 0
    while money >= 5500:
        money -= 5500
        result1 += 1

    answer.append(result1)
    answer.append(money)
    return answer

# 나이 출력
def solution3(age):

    answer = 2023 - age

    return answer

# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    return num_list