# 최대값 만들기 (1)
def solution(numbers):
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    return answer

# 팩토리얼
import math
def solution(n):
    k = 10
    while n < math.factorial(k):
        k -= 1
    return k

# 주사위의 갯수
def solution(box, n):
    answer = 0

    answer = (box[0] //  n) * (box[1] // n) * (box[2] // n)
    return answer

# 합성수 찾기
def solution(n):
    answer = 0
    num = []

    count = 0
    for i in range(2, n+1):
        for j in range(1, i+1):

            if i % j == 0:
                num.append(i)
        if num.count(i) >= 3:
            answer += 1
    return answer
