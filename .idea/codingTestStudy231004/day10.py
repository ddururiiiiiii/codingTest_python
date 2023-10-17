# 문자열의 앞의 n글자
def solution(my_string, n):
    answer = my_string[:n]
    return answer

# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 0
    arr = []
    text = ''
    for i in range(len(my_string)):
        arr.append(my_string[:i])

    return 1 if is_prefix in arr else 0


# return int(my_string.startswith(is_prefix))


# 문자열 뒤집기
def solution(my_string, s, e):
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return answer

# 세로읽기
def solution(my_string, m, c):
    answer = ''

    for i in range(0, len(my_string), m):
        answer += my_string[i+c-1]

    return answer
# s[c-1::m]


# qr code
def solution(q, r, code):
    answer = ''

    for i in range(len(code)):
        if i % q == r :
            answer += code[i]

    return answer

# return code[r::q]