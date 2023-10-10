# 코드 처리하기
def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)) :
        if mode == 0 :
            if code[idx] != '1' and idx % 2 == 0:
                answer += str(code[idx])
            elif code[idx] == '1' :
                mode = 1
        elif mode == 1:
            if code[idx] != '1' and idx % 2 != 0 :
                answer += str(code[idx])
            elif code[idx] == '1' :
                mode = 0

    if answer == '':
        answer = 'EMPTY'
    return answer

# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    num1 = 0
    for i in range(len(included)):
        answer = a + (d * i)
        if included[i]:
            num1 += answer

    return num1

# 주사위게임2
def solution(a, b, c):
    answer = 0

    if a == b and b == c and a == c :
        answer =  (a+b+c)  * ((a**2) + (b**2) + (c**2)) * ((a**3) + (b**3) + (c**3))
    elif a != b and b != c and a != c :
        answer = a + b + c
    else :
        answer =  (a+b+c)  * ((a**2) + (b**2) + (c**2))

    return answer

# 원소들의 곱과 합
def solution(num_list):
    answer = 0
    num1 = 1;
    num2 = 0;

    for i in num_list :
        num1 *= i
        num2 += i

    if int(num1) < int(num2**2):
        answer = 1
    else:
        answer = 0

    return answer

# 이어 붙인 수
def solution(num_list):
    answer = 0
    evl = "";
    odd = "";

    for i in num_list :
        if i % 2 == 0:
            evl += str(i)
        else:
            odd += str(i)

    answer = int(evl) + int(odd)
    return answer