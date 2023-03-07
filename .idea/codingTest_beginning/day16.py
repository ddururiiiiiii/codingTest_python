# 편지
def solution(message):
    return len(answer)*2

# 배열의 유사도
def solution(s1, s2):
    answer = 0

    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer

# 문자열 계산하기
def solution(my_string):
    return eval(my_string)

# 가장 큰 수 찾기 (1)
def solution(array):
    answer = []

    list = sorted(array, reverse=True)
    answer.append(list[0])

    for index, val in enumerate(array):
        if val == list[0]:
            answer.append(index)

    return answer

# 가장 큰 수 찾기 (2)
def solution(array):
    return [max(array), array.index(max(array))]