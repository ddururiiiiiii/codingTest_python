# 문자열 뒤집기
def solution1(my_string):
    answer = ''

    # 문자열을 리스트로
    myStringList = list(my_string)

    #리스트를 역순으로
    myStringList.reverse()

    # 리스트를 문자열로
    answer = ''.join(myStringList)

    return answer

# 직각삼각형 출력하기
n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

# 짝수 홀수 개수
def solution2(num_list):
    answer = [0, 0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else :
            answer[1] += 1

    return answer

# 문자 반복 출력하기
def solution3(my_string, n):
    answer = ''

    for i in list(my_string):
        answer += i * n
    return answer