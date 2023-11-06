# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)

# 배열 비교하기
def solution(arr1, arr2):
    answer = 0
    sum1 = 0
    sum2 = 0

    if len(arr1) == len(arr2):

        for i in arr1:
            sum1 += i
        for j in arr2:
            sum2 += j

        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        else :
            return 0

    else :
        if len(arr1) > len(arr2) :
            return 1
        else :
            return -1
    return answer

# 문자열 묶기
def solution(strArr):
    answer = [len(i) for i in strArr]

    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))

    return max(tmp)

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    answer = []

    if len(arr) % 2== 0: # 짝수
        for i, v in enumerate(arr):
            if i % 2 == 1 :
                arr[i] = v + n
    else:
        for i, v in enumerate(arr):
            if i % 2 == 0 :
                arr[i] = v + n

    return arr


# 뒤에서 5등까지
def solution(num_list):
    answer = []

    num_list.sort();

    for i in range(0, 5):
        answer.append(num_list[i])

    return answer