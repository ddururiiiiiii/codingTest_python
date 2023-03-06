# 영어가 싫어요
def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))

    return int(numbers)

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

# 한 번만 등장한 문자
def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    return ''.join(sorted(answer))

# 약수 구하기
def solution(n):
    answer = []

    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer