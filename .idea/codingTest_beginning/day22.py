# 겹치는 선분의 길이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 유한소수 판별하기
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

#저주의 숫자3
def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
    return answer

