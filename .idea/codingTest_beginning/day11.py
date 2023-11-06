# 문자 개수 세기
def solution(my_string):
    abcArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numArr = [0] * len(abcArr)
    answer = []

    for i in my_string:
        for j in range(len(abcArr)):
            if i == abcArr[j]:
                numArr[j] = numArr[j]+1
                print(abcArr[j], numArr)

    return numArr

# 배열 만들기 1
def solution(n, k):
    answer = []

    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)


    return answer

# 글자 지우기
def solution(my_string, indices):
    answer = ''

    for index, value in enumerate(my_string):
        if index not in indices :
            answer += value

    return answer

# 카운트 다운
def solution(start, end_num):
    answer = []

    for i in range(start, end_num-1, -1):
        answer.append(i)
    return answer

# 가까운 1 찾기
def solution(arr, idx):
    answer = 0
    temp = []
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            temp.append(i)

    if len(temp) == 0 :
        answer = -1
    else :
        answer = min(temp)

    return answer