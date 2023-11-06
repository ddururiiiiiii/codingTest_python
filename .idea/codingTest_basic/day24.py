# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div+mod
    return answer

# 이진수 더하기
def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    answer = bin(a + b)
    return answer[2:]

# k의 개수
def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer

# A로 B 만들기
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0