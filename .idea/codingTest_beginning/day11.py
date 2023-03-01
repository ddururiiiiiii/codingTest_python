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
