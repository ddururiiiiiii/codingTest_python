# 리스트 자르기
def solution(n, slicer, num_list):
    a, b, c = slicer

    if n == 1:
        result = num_list[:b+1]
    elif n == 2:
        result = num_list[a:]
    elif n == 3:
        result = num_list[a:b+1]
    elif n == 4:
        result = num_list[a:b+1:c]
    return result

# 첫번째로 나오는 음수
def solution(num_list):
    answer = 0

    for i, v in enumerate(num_list):
        if v < 0:
            return i
        else :
            answer = -1

    return answer

# 배열 만들기 3
def solution(arr, intervals):
    answer = []

    for interval in intervals :
        answer += arr[interval[0]:interval[1]+1]
    return answer

# 2의 영역
def solution(arr):
    answer = []
    numTwo = []

    for i, v in enumerate(arr):
        if v == 2 :
            numTwo.append(i)

    if(len(numTwo) == 0): return [-1]
    else :
        answer = arr[numTwo[0]:numTwo[-1]+1]

    return answer

# 배열 조각하기
def solution(arr):
    answer = []
    numTwo = []

    for i, v in enumerate(arr):
        if v == 2 :
            numTwo.append(i)

    if(len(numTwo) == 0): return [-1]
    else :
        answer = arr[numTwo[0]:numTwo[-1]+1]

    return answer