# 배열 자르기
def solution(numbers, num1, num2):
    answer = []

    answer = numbers[num1:num2+1]

    return answer

# 외계행성의 나이
def solution(age):
    answer = ''
    word = ["a", "b","c","d","e","f","g","h","i","j"]


    for i in str(age):
        answer += word[int(i)]
    return answer

# 진료순서 정하기
def solution(emergency):
    answer = []

    sortList = sorted(emergency, reverse = True)

    for i in emergency :
        answer.append(sortList.index(i)+1)


    return answer

# 순서쌍의 개수
def solution(n):
    answer =[]

    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
    return len(answer)