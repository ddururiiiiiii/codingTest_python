# 문자열안에 문자열
def solution(str1, str2):
    answer = 0

    if str2 in str1:
        answer = 1
    else:
        answer = 2


    return answer

# 문자열 정렬하기
def solution(my_string):
    my_string = sorted(list(my_string.lower()))
    answer = ''.join(my_string)

    return answer

# 세균 증식
def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer

# 제곱수 판별하기
# 이번 문제는 n ** (1/2)가 제곱근이라는 것과,
# 숫자를 1로 나눴을 때 나머지가 0이면 정수라는 것
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2