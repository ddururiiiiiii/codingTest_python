# 배열 만들기5
def solution(intStrs, k, s, l):
    answer = []

    for intStr in intStrs:
        if int(intStr[s:s+l]) > k :
            answer.append(int(intStr[s:s+l]))
    return answer

# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''

    # enumerate : 인수와 값을 동시에 접근
    for index, val in enumerate(parts):
        print(index, val)
        answer += my_strings[index][val[0]:val[1]+1]

    return answer

# 문자열의 뒤의 n글자
def solution(my_string, n):
    answer = ''
    answer = my_string[len(my_string) - n:]
    return answer
# return my_string[-n:]

# 접미사 배열
def solution(my_string):
    answer = []

    for i in range(len(my_string)):
        answer.append(my_string[i:])
        answer.sort()
    return answer

# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = 0
    answer_list = []

    for i in range(len(my_string)):
        answer_list.append(my_string[i:])

    return 1 if is_suffix in answer_list else 0