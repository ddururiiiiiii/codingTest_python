# n 번째 원소부터
def solution(num_list, n):
    answer = []

    for i in range(n-1, len(num_list)) :
        answer.append(num_list[i])

    return answer

# 순서 바꾸기
def solution(num_list, n):
    answer = []
    answer = num_list[n:] + num_list[:n]

    return answer

# 왼쪽 오른쪽
def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        if str_list[i]=='l':
            return str_list[:i]
        elif str_list[i]=='r':
            return str_list[i+1:]

    return answer

# n번째 원소까지
def solution(num_list, n):
    answer = []

    answer = num_list[:n]
    return answer

# n개 간격의 원소들
def solution(num_list, n):
    answer = []

    answer = num_list[::n]
    return answer

