# 문자열 섞기
def solution(str1, str2):
    answer = ''

    for i in range(0, len(str1)):
        answer += str1[i] + str2[i]
    return answer


# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''

    for i in arr:
        answer += str(i)
    return answer

# return ''.join(arr)

# 문자열 곱하기
def solution(my_string, k):
    answer = ''

    for i in range(k):
        answer += my_string
    return answer

# return my_string*k


# 더 크게 합치기
def solution(a, b):
    answer = 0

    str1 = str(a) + str(b)
    str2 = str(b) + str(a)

    if int(str1) > int(str2):
        answer = int(str1)
    elif int(str1) < int(str2):
        answer =  int(str2)
    else :
        answer =  int(str1)

    return answer

# return int(max(f"{a}{b}", f"{b}{a}"))


# 두 수의 연산값 비교하기
def solution(a, b):
    # string 형태로 더한 것
    stra, strb = str(a), str(b)
    str1 = int(stra+strb)

    # int 형태로 계산한 것
    inta, intb = int(a), int(b)
    int1 = 2 * inta *intb


    if str1 != int1: # 둘의 값이 같지 않을 경우 최대값 구함
        return int(max(str1, int1))
    else : # 둘의 값이 같을 경우 string 형태 리턴
        return int(str1)
    return answer

# return max(int(str(a) + str(b)), 2 * a * b)