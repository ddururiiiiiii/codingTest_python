### 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

def solution(myString, pat):
    answer = myString.rsplit(pat, 1)[0] + pat
    return answer

### 문자열이 몇 번 등장하는지 세기

def solution(myString, pat):
    count = 0
    index = myString.find(pat)

    while index != -1:
        count += 1
        index = myString.find(pat, index + 1)

    return count

### ab 제거하기
def solution(strArr):
    answer = []

    for i in strArr:
        if i.find("ad") == -1 :
            answer.append(i)


    return answer

### 공백으로 구분하기 1
def solution(my_string):
    answer = my_string.split(" ")
    return answer

### 공백으로 구분하기 2
def solution(my_string):
    answer = my_string.split()
    return answer