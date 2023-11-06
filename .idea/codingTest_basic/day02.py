import math
import numpy as np

# 두 수의 나눗셈
def solution1(num1, num2):
    answer = -1

    answer = 0
    answer = int(num1 / num2 * 1000)
    return answer

# 숫자 비교하기
def solution2(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer

# 분수의 덧셈
def solution3(denum1, num1, denum2, num2):
    top = denum1 * num2 + denum2 * num1
    bottom = num1 * num2
    n = math.gcd(top, bottom) # 최대공약수
    if n == 1:
        return [top, bottom]
    else:
        return [top/n, bottom/n]


# 배열 두배 만들기
def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(i*2)
    return answer

# def main():
#     print("Main Function")
#     solution1(3, 4)
#     solution2(4, 1)
#     solution3(3, 4)
#     solution4(10, 4)
#
# if __name__ == "__main__":
#     main()
#

