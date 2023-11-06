# 종이 자르기
def solution(M, N):
    return (M * N) - 1

# 문자열 밀기
def solution(A,B):
    for cnt in range(len(A)):
        if A == B:
            return cnt
        A = A[-1] + A[:-1]

    return -1

# 다음에 올 숫자
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer

# 연속된 수의 합
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
