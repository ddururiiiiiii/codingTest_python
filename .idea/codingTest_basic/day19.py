# 중복된 숫자 개수
def solution(array, n):
    answer = 0

    for i in array:
        if i == n:
            answer += 1
    return answer

# 다른 풀이
def solution(array, n):
    return array.count(n)

# 7의 개수
def solution(array):
    return str(array).count("7")

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1

    return answer

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for _ in range(0, len(my_str), n):
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer