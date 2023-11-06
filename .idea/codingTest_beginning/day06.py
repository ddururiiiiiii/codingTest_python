# 마지막 두 원소
def solution(num_list):
    answer = []

    lastNum1 = num_list[-1]
    lastNum2 = num_list[-2]

    if lastNum1 > lastNum2 :
        num_list.append(lastNum1 - lastNum2)
    else :
        num_list.append(lastNum1 * 2)


    return num_list

# 수 조작하기 1
def solution(n, control):
    answer = 0


    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10

    return n

# 수 조작하기 2
def solution(numLog):
    answer = ''

    for i in range(1, len(numLog)) :
        if numLog[i] - numLog[i-1]  == 1 :
            answer += 'w'
        if numLog[i-1] - numLog[i]  == 1 :
            answer += 's'
        if numLog[i] - numLog[i-1]  == 10 :
            answer += 'd'
        if numLog[i-1] - numLog[i]  == 10 :
            answer += 'a'
    return answer

# 수열과 구간 쿼리 3
def solution(arr, queries):
    answer = []

    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]

    return arr

# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []

    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]

    return arr