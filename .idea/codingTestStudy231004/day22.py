# 0 떼기
def solution(n_str):
    return str(int(n_str))

# 두 수의 합
def solution(a, b):
    answer = int(a) + int(b)
    return str(answer)

# 문자열로 변환
def solution(n):
    return str(n)


# 배열의 원소 삭제하기
def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

# 부분 문자열인지 확인하기
def solution(my_string, target):
    answer = 0

    if target in my_string:
        answer = 1
    else :
        answer = 0


    return answer