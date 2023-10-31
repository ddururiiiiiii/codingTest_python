# 세 개의 구분자
def solution(myStr):
    answer = []
    myStr3 = []
    myStr4 = []
    myStr = myStr.split("a");
    for i in myStr:
        myStr2 = i.split("b")
        for j in myStr2:
            if j != "":
                myStr3.append(j)

    for i in myStr3:
        test = i.split("c")
        for j in test :
            if j != "":
                myStr4.append(j)

    if len(myStr4) == 0 :
        myStr4.append("EMPTY")
    else :
        return myStr4
    return myStr4


# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []

    for i in arr:
        for j in range(0, i):
            answer.append(i)

    return answer


# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []

    for i, v in enumerate(flag):
        if v :
            for j in range(0, arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(0, arr[i]):
                answer.pop();



    return answer


# 배열 만들기 6
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        else :
            if answer[-1] == arr[i]:
                answer.pop();
            else:
                answer.append(arr[i])

    if len(answer) == 0:
        return [-1]


    return answer

# 무작위로 K개의 수 뽑기
def solution(arr, k):
    answer = []

    for i in arr:
        if i not in answer and len(answer) < k :
            answer.append(i)

    if len(answer) < k :
        for i in range(0, k - len(answer)):
            answer.append(-1)

    return answer