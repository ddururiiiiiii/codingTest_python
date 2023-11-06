# 컨트롤 제트
def solution(s):
    answer = []

    for i in s.split():
        if i == "Z":
            answer.pop()
            continue
        answer.append(int(i))

    return sum(answer)

# 배열 원소의 길이
def solution(strlist):
    answer = []

    for i in strlist:
        answer.append(len(i))
    return answer

# 중복된 문자 제거
def solution(my_string):
    answer = "".join(dict.fromkeys(my_string))
    return answer

# 삼각형의 완성조건
def solution(sides):
    answer = 0

    sides.sort(reverse=True)

    if sides[0] < sides[1] + sides[2]:
        answer = 1
    else :
        answer = 2

    return answer

