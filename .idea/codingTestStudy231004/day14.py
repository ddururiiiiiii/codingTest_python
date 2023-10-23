# 홀수 vs 짝수
def solution(num_list):
    answer = 0
    odd = 0
    even = 0

    for i, v in enumerate(num_list):
        if i % 2 == 0:
            even += num_list[i];
        else :
            odd += num_list[i];

    if even > odd :
        return even
    else :
        return odd

    return answer
# return max(sum(num_list[::2]), sum(num_list[1::2]))

# 5명씩
def solution(names):
    answer = []

    for i in range(0, len(names), 5):
        answer.append(names[i])

    return answer
# return names[::5]

# 할 일 목록
def solution(todo_list, finished):
    answer = []

    for i, v in enumerate(todo_list):
        if not finished[i] :
            answer.append(todo_list[i])
    return answer

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0

    for i in numbers:
        if answer > n:
            return answer
        else :
            answer += i

    return answer

#  수열과 구간 쿼리 1
def solution(arr, queries):
    for l,r in queries:
        print(l, r)
        for i in range(l,r+1): arr[i]+=1
    return arr