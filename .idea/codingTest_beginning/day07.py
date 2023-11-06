# 수열과 구간 쿼리 4
def solution(arr, queries):
    answer = []

    for query in queries:
        print(query)
        for num in range(query[0], query[1]+1) :
            if num % query[2] == 0:
                arr[num] = arr[num] + 1

    return arr

# 배열 만들기 2
def solution(l, r):
    answer = []

    for num in range(l, r+1):
        if not set(str(num)) - {'0','5'}:
            answer.append(num)

    if answer == []:
        answer.append(-1)
    return answer

# 카운트 업
def solution(start_num, end_num):
    answer = []

    for num in range(start_num, end_num+1):
        answer.append(num)
    return answer


#콜라츠 수열 만들기
def solution(n):
    answer = [n]

    while n != 1:
        if n % 2 == 0 :
            n //= 2
        else:
            n = 3 * n + 1

        answer.append(n)

    return answer

# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0;

    while i < len(arr) :
        if stk == [] :
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i] :
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            del stk[-1]

    return stk