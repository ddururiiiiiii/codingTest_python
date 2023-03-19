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