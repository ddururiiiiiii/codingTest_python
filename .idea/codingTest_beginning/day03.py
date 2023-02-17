# 나머지 구하기

def solution1(num1, num2):
    answer = num1 % num2;
    return answer

# 중앙값 구하기
def solution2(array):
    answer = 0

    # 오름차순 정렬
    array.sort()
    answer = array[len(array) // 2]
    return answer


# 최빈값 구하기
def solution3(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

# 짝수는 싫어요

def solution4(n):
    return [i for i in range(1, n+1, 2)]