# 뒤에서 5등 위로
def solution(num_list):
    answer = []
    num_list.sort();
    return num_list[5:]

# 전국 대회 선발 고사
def solution(rank, attendance):
    answer = 0
    tmp = []
    for i, v in enumerate(rank):
        if attendance[i] == True:
            tmp.append(rank[i]);

    tmp.sort();
    a = 0
    b = 0
    c = 0
    for i, v in enumerate(rank):
        if v == tmp[0]:
            a = i
        elif v == tmp[1]:
            b = i
        elif v == tmp[2]:
            c = i

    return 10000 * a + 100 * b + c


# 정수 부분
def solution(flo):
    answer = 0
    return int(flo)


# 문자열 정수의 합
def solution(num_str):
    answer = 0

    for i in num_str:
        answer += int(i)

    return answer


# 문자열을 정수로 변환하기
def solution(n_str):
    answer = 0
    return int(n_str)