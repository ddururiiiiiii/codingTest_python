# 모음 제거
import re

def solution(my_string):
    answer = ''

    answer = re.sub("a|e|i|o|u", "", my_string)
    return answere.sub(r"a|e|i|o|u", "", my_string)

# 문자열 정렬하기 (1)
import re

def solution(my_string):
    answer2 = list(re.sub(r'[^0-9]', '', my_string))
    answer2.sort()
    answer = [int (i) for i in answer2]
    return answer

# 숨어있는 숫자의 덧셈 (1)
import re

def solution(my_string):
    answer2 = list(re.sub(r'[^0-9]', '', my_string))
    answer2 = [int (i) for i in answer2]
    answer = sum(answer2)
    return answer

# 소인수분해
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    return list(dict.fromkeys(answer))