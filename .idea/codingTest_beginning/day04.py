# n의 배수
def solution(num, n):
    answer = 0

    if num % n == 0 :
        answer = 1;
    else :
        answer = 0;

    return answer

# 공배수
def solution(number, n, m):
    answer = 0

    if number % n == 0 and number % m == 0 :
        answer = 1;
    else :
        answer = 0;

    return answer

# 홀짝에 따라 다른 값 반환하기
import math

def solution(n):
    answer = 0

    if n % 2 != 0:
        for i in range(1, n+1):
            if i % 2 != 0 :
                answer += i;
    else :
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += math.pow(i, 2);

    return answer

# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    answer = 0


    if flag :
        answer = int(a + b)
    else :
        answer = int(a - b)

    return answer

# 조건 문자열
def solution(ineq, eq, n, m):
    answer = 0

    if eq == "!" :
        if ineq == "<" :
            answer = int(n<m)
        else:
            answer = int(n>m)
    else:
        if ineq == "<" :
            answer = int(n<=m)
        else:
            answer = int(n>=m)

    return answer